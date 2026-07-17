from PySide6 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg
from IB64C_UI.UI.IB64C_UI import IB64C_Screen
from IB64C_Core.IB64C_Core_Logic import convertToBase64, SearchDirectory
import os


class WorkerThread(qtc.QObject):
    finished = qtc.Signal()
    success = qtc.Signal(str)
    error = qtc.Signal(str)

    def __init__(self, input_directory, output_directory, file_type):
        super().__init__()
        self.input_directory = input_directory
        self.output_directory = output_directory
        self.file_type = file_type

    def run(self):
        imgs = SearchDirectory(
            directory_path=self.input_directory, file_type=self.file_type
        )
        
        if not imgs:
            self.error.emit("No images found with the specified type.")
            self.finished.emit()
            return
        
        is_converted, file_name = convertToBase64(imgs=imgs, output_directory=self.output_directory)
        if is_converted:
            self.success.emit(f"{file_name} File generated successfully.")
            self.finished.emit()
            return


class IB64C_Logic(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = IB64C_Screen()

        self.ui.ConvertButton.clicked.connect(self.convert_to_base64)
        self.ui.InputBrowseAction.triggered.connect(
            lambda checked: self.browse_directory(operation="input")
        )
        self.ui.OutputBrowseAction.triggered.connect(
            lambda checked: self.browse_directory(operation="output")
        )

        self.ui.DirectoryInput.textChanged.connect(
            lambda text: self.live_validate(self.ui.DirectoryInput)
        )

        self.ui.DirectoryOutput.textChanged.connect(
            lambda text: self.live_validate(self.ui.DirectoryOutput)
        )

        self.ui.DirectoryInput.editingFinished.connect(
            lambda: self.live_validate(self.ui.DirectoryInput)
        )

        self.ui.DirectoryOutput.editingFinished.connect(
            lambda: self.live_validate(self.ui.DirectoryOutput)
        )

    def convert_to_base64(self):
        self.directory_input_value = self.ui.DirectoryInput.text().strip()
        self.directory_output_value = self.ui.DirectoryOutput.text().strip()
        self.file_type = self.ui.FileTypeCombo.currentText()

        if not (
            self.live_validate(self.ui.DirectoryInput)
            and self.live_validate(self.ui.DirectoryOutput)
        ):
            return

        self.Thread_ = qtc.QThread()
        self.Worker = WorkerThread(
            input_directory=self.directory_input_value,
            output_directory=self.directory_output_value,
            file_type=self.file_type,
        )
        self.Worker.moveToThread(self.Thread_)

        self.Thread_.started.connect(self.Worker.run)
        self.Worker.finished.connect(self.Thread_.quit)
        self.Worker.success.connect(self.show_success)
        self.Worker.error.connect(self.show_error)
        self.Worker.finished.connect(self.Worker.deleteLater)
        self.Thread_.start()

        self.LoadingMovie = qtg.QMovie("Assets/loadingIcon.gif")
        self.LoadingMovie.setScaledSize(qtc.QSize(20, 20))
        self.LoadingMovie.frameChanged.connect(
            lambda: self.ui.ConvertButton.setIcon(self.LoadingMovie.currentPixmap())
        )
        self.LoadingMovie.start()

        self.Thread_.finished.connect(lambda: self.ui.ConvertButton.setEnabled(True))
        self.ui.ConvertButton.setEnabled(False)

    def browse_directory(self, operation):
        selected_directory = qtw.QFileDialog.getExistingDirectory(
            self, f"Select {operation} Folder"
        )
        if selected_directory:
            if operation == "input":
                self.ui.DirectoryInput.setText(selected_directory)
            else:
                self.ui.DirectoryOutput.setText(selected_directory)

    def live_validate(self, line_edit: qtw.QLineEdit, normal: bool = False):
        path_text = line_edit.text().strip()

        if normal:
            line_edit.setProperty("state", None)
            self.refresh_ui(line_edit)
            return True

        if path_text == "" or not os.path.exists(path=path_text):
            line_edit.setProperty("state", "DirectoryInvalid")
            self.refresh_ui(line_edit)
            return False

        line_edit.setProperty("state", "DirectoryValid")
        self.refresh_ui(line_edit)
        return True

    def refresh_ui(self, widget):
        widget.style().unpolish(widget)
        widget.style().polish(widget)

    def show_error(self, message):
        self.ui.FeedbackLabel.setText(message)
        self.ui.FeedbackFrame.setProperty("state", "error")
        self.refresh_ui(self.ui.FeedbackFrame)
        self.ui.FeedbackFrame.show()
        self.ui.center()
        self.setFocus()

        self.revert_button(button=self.ui.ConvertButton, icon_variable="LoadingMovie", movie_icon=self.LoadingMovie)
        return

    def show_success(self, message):
        self.ui.DirectoryInput.clear()
        self.ui.DirectoryOutput.clear()

        self.ui.FeedbackLabel.setText(message)
        self.ui.FeedbackPixmap = qtg.QPixmap("Assets/successIcon.png")
        self.ui.FeedbackPixmapScaled = self.ui.FeedbackPixmap.scaled(
            20,
            20,
            qtc.Qt.AspectRatioMode.KeepAspectRatio,
            qtc.Qt.TransformationMode.SmoothTransformation,
        )
        self.ui.FeedbackIcon.setPixmap(self.ui.FeedbackPixmapScaled)
        self.ui.FeedbackFrame.setProperty("state", "success")
        self.ui.FeedbackFrame.show()
        self.ui.center()
        self.setFocus()
        
        self.ui.FileTypeCombo.setCurrentIndex(0)

        self.revert_button(button=self.ui.ConvertButton, icon_variable="LoadingMovie", movie_icon=self.LoadingMovie)

        self.live_validate(line_edit=self.ui.DirectoryInput, normal=True)
        self.live_validate(line_edit=self.ui.DirectoryOutput, normal=True)
        self.refresh_ui(self.ui.FeedbackFrame)
        return

    def revert_button(
        self, button: qtw.QPushButton, icon_variable: str, movie_icon: qtg.QMovie
    ):
        if hasattr(self, icon_variable):
            movie_icon.stop()
            
        button.setIcon(qtg.QIcon("Assets/codeIcon.png"))
        button.setText("Convert to Base64")
        return

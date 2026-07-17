from PySide6 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg
from IB64C_UI.Theme.Theme import app_styles


class IB64C_Screen(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 500
        self.setFixedWidth(self.width)
        self.setWindowTitle("Image Base64 Converter")
        self.setWindowIcon(qtg.QIcon("Assets/app_icon.ico"))

        self.setupUI()
        self.setFocus()
        self.setStyleSheet(app_styles)

        self.center()

    def center(self):
        self.adjustSize()

        QRect = self.frameGeometry()
        CenterPoint = self.screen().availableGeometry().center()

        QRect.moveCenter(CenterPoint)

        self.move(QRect.topLeft())

    def setupUI(self):
        self.CentralWidget = qtw.QWidget()
        self.setCentralWidget(self.CentralWidget)

        self.MainLayout = qtw.QVBoxLayout()
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setSpacing(0)

        self.CentralWidget.setLayout(self.MainLayout)

        self.BodyLayout = qtw.QVBoxLayout()
        self.BodyLayout.setContentsMargins(30, 30, 30, 30)
        self.BodyLayout.setSpacing(30)

        self.BodyFrame = qtw.QFrame()
        self.BodyFrame.setObjectName("BodyFrame")
        self.BodyFrame.setLayout(self.BodyLayout)

        self.MainLayout.addWidget(self.BodyFrame)

        self.setHeaderFrame()
        self.setInputsFrame()
        self.setFeedbackFrame()
        self.setInfoFrame()

    def setHeaderFrame(self):
        self.HeaderLayout = qtw.QHBoxLayout()
        self.HeaderLayout.setContentsMargins(0, 0, 0, 0)
        self.HeaderLayout.setSpacing(10)

        self.HeaderFrame = qtw.QFrame()
        self.HeaderFrame.setObjectName("HeaderFrame")
        self.HeaderFrame.setLayout(self.HeaderLayout)

        self.HeaderIcon = qtw.QLabel()
        self.HeaderIconPixmap = qtg.QPixmap("Assets/codeIcon.png")
        self.HeaderIconPixmapScaled = self.HeaderIconPixmap.scaled(
            30,
            30,
            qtc.Qt.AspectRatioMode.KeepAspectRatio,
            qtc.Qt.TransformationMode.SmoothTransformation,
        )
        self.HeaderIcon.setPixmap(self.HeaderIconPixmapScaled)

        self.HeaderIconLayout = qtw.QVBoxLayout()
        self.HeaderIconLayout.setContentsMargins(0, 0, 0, 0)
        self.HeaderIconLayout.setSpacing(0)
        self.HeaderIconLayout.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)

        self.HeaderIconFrame = qtw.QFrame()
        self.HeaderIconFrame.setObjectName("HeaderIconFrame")
        self.HeaderIconFrame.setFixedSize(50, 50)
        self.HeaderIconFrame.setLayout(self.HeaderIconLayout)

        self.HeaderIconLayout.addWidget(self.HeaderIcon)

        self.HeaderInnerLayout = qtw.QVBoxLayout()
        self.HeaderInnerLayout.setContentsMargins(0, 0, 0, 0)
        self.HeaderInnerLayout.setSpacing(0)

        self.HeaderInnerFrame = qtw.QFrame()
        self.HeaderInnerFrame.setObjectName("HeaderInnerFrame")
        self.HeaderInnerFrame.setLayout(self.HeaderInnerLayout)

        self.HeaderInnerLabel = qtw.QLabel("Image Base64 Converter")
        self.HeaderInnerLabel.setObjectName("HeaderInnerLabel")

        self.HeaderInnerSecondaryLabel = qtw.QLabel(
            "Convert images to Python base64 file"
        )
        self.HeaderInnerSecondaryLabel.setObjectName("HeaderInnerSecondaryLabel")

        self.HeaderInnerLayout.addWidget(self.HeaderInnerLabel)
        self.HeaderInnerLayout.addWidget(self.HeaderInnerSecondaryLabel)

        self.HeaderLayout.addWidget(self.HeaderIconFrame)
        self.HeaderLayout.addWidget(self.HeaderInnerFrame)
        self.HeaderLayout.addStretch()

        self.BodyLayout.addWidget(self.HeaderFrame)

    def setInputsFrame(self):
        self.InputsLayout = qtw.QVBoxLayout()
        self.InputsLayout.setContentsMargins(0, 0, 0, 0)
        self.InputsLayout.setSpacing(20)

        self.InputsFrame = qtw.QFrame()
        self.InputsFrame.setLayout(self.InputsLayout)
        self.InputsFrame.setFixedHeight(340)

        self.DirectoryInputIcon = qtw.QLabel()
        self.DirectoryInputPixmap = qtg.QPixmap("Assets/inputIcon.png")
        self.DirectoryInputPixmapScaled = self.DirectoryInputPixmap.scaled(
            20,
            20,
            qtc.Qt.AspectRatioMode.KeepAspectRatio,
            qtc.Qt.TransformationMode.SmoothTransformation,
        )

        self.DirectoryInputIcon.setPixmap(self.DirectoryInputPixmapScaled)

        self.DirectoryInputLabel = qtw.QLabel("Input Directory")
        self.DirectoryInputLabel.setObjectName("DirectoryInputLabel")

        self.DirectoryInput = qtw.QLineEdit()
        self.DirectoryInput.setPlaceholderText("/path/to/images")

        self.DirectoryInputPlaceholder = self.DirectoryInput.palette()
        self.DirectoryInputPlaceholder.setColor(
            qtg.QPalette.ColorRole.PlaceholderText, qtg.QColor("#64748b")
        )

        self.DirectoryInput.setPalette(self.DirectoryInputPlaceholder)

        self.DirectoryInputPathSelectorIcon = qtg.QIcon("Assets/inputIcon.png")

        self.InputBrowseAction = self.DirectoryInput.addAction(
            self.DirectoryInputPathSelectorIcon,
            qtw.QLineEdit.ActionPosition.TrailingPosition,
        )

        self.InputActionButton = self.DirectoryInput.findChild(qtw.QToolButton)
        if self.InputActionButton:
            self.InputActionButton.setCursor(qtc.Qt.CursorShape.PointingHandCursor)

        self.DirectoryInputLayout = qtw.QVBoxLayout()
        self.DirectoryInputLayout.setContentsMargins(0, 0, 0, 0)
        self.DirectoryInputLayout.setSpacing(10)

        self.DirectoryInputFrame = qtw.QFrame()
        self.DirectoryInputFrame.setLayout(self.DirectoryInputLayout)

        self.DirectoryInputLabelLayout = qtw.QHBoxLayout()
        self.DirectoryInputLabelLayout.setContentsMargins(0, 0, 0, 0)
        self.DirectoryInputLabelLayout.setSpacing(5)

        self.DirectoryInputLabelFrame = qtw.QFrame()
        self.DirectoryInputLabelFrame.setLayout(self.DirectoryInputLabelLayout)

        self.DirectoryInputLabelLayout.addWidget(self.DirectoryInputIcon)
        self.DirectoryInputLabelLayout.addWidget(self.DirectoryInputLabel)
        self.DirectoryInputLabelLayout.addStretch()

        self.DirectoryInputLayout.addWidget(self.DirectoryInputLabelFrame)
        self.DirectoryInputLayout.addWidget(self.DirectoryInput)

        self.FileTypeComboIcon = qtw.QLabel()
        self.FileTypePixmap = qtg.QPixmap("Assets/fileTypeIcon.png")
        self.FileTypePixmapScaled = self.FileTypePixmap.scaled(
            20,
            20,
            qtc.Qt.AspectRatioMode.KeepAspectRatio,
            qtc.Qt.TransformationMode.SmoothTransformation,
        )

        self.FileTypeComboIcon.setPixmap(self.FileTypePixmapScaled)

        self.FileTypeComboLabel = qtw.QLabel("File Type")
        self.FileTypeComboLabel.setObjectName("FileTypeComboLabel")

        self.FileTypeCombo = qtw.QComboBox()
        self.FileTypeCombo.addItems(
            ["PNG", "JPG", "JPEG", "GIF", "BMP", "WebP", "SVG", "ALL"]
        )

        self.FileTypeCombo.setView(qtw.QListView())
        self.FileTypeCombo.view().window().setAttribute(
            qtc.Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self.FileTypeComboLayout = qtw.QVBoxLayout()
        self.FileTypeComboLayout.setContentsMargins(0, 0, 0, 0)
        self.FileTypeComboLayout.setSpacing(10)

        self.FileTypeComboFrame = qtw.QFrame()
        self.FileTypeComboFrame.setLayout(self.FileTypeComboLayout)

        self.FileTypeComboLabelLayout = qtw.QHBoxLayout()
        self.FileTypeComboLabelLayout.setContentsMargins(0, 0, 0, 0)
        self.FileTypeComboLabelLayout.setSpacing(5)

        self.FileTypeComboLabelFrame = qtw.QFrame()
        self.FileTypeComboLabelFrame.setLayout(self.FileTypeComboLabelLayout)

        self.FileTypeComboLabelLayout.addWidget(self.FileTypeComboIcon)
        self.FileTypeComboLabelLayout.addWidget(self.FileTypeComboLabel)
        self.FileTypeComboLabelLayout.addStretch()

        self.FileTypeComboLayout.addWidget(self.FileTypeComboLabelFrame)
        self.FileTypeComboLayout.addWidget(self.FileTypeCombo)

        self.DirectoryOutputIcon = qtw.QLabel()
        self.DirectoryOutputPixmap = qtg.QPixmap("Assets/outputIcon.png")
        self.DirectoryOutputPixmapscaled = self.DirectoryOutputPixmap.scaled(
            20,
            20,
            qtc.Qt.AspectRatioMode.KeepAspectRatio,
            qtc.Qt.TransformationMode.SmoothTransformation,
        )
        self.DirectoryOutputIcon.setPixmap(self.DirectoryOutputPixmapscaled)

        self.DirectoryOutputLabel = qtw.QLabel("Output Directory")
        self.DirectoryOutputLabel.setObjectName("DirectoryOutputLabel")

        self.DirectoryOutput = qtw.QLineEdit()
        self.DirectoryOutput.setPlaceholderText("/path/to/output")

        self.DirectoryOutputPlaceholder = self.DirectoryOutput.palette()
        self.DirectoryOutputPlaceholder.setColor(
            qtg.QPalette.ColorRole.PlaceholderText, qtg.QColor("#64748b")
        )

        self.DirectoryOutput.setPalette(self.DirectoryOutputPlaceholder)

        self.DirectoryOutputPathSelectorIcon = qtg.QIcon(
            "Assets/inputIcon.png"
        )

        self.OutputBrowseAction = self.DirectoryOutput.addAction(
            self.DirectoryOutputPathSelectorIcon,
            qtw.QLineEdit.ActionPosition.TrailingPosition,
        )

        self.OutputActionButton = self.DirectoryOutput.findChild(qtw.QToolButton)
        if self.OutputActionButton:
            self.OutputActionButton.setCursor(qtc.Qt.CursorShape.PointingHandCursor)

        self.DirectoryOutputLayout = qtw.QVBoxLayout()
        self.DirectoryOutputLayout.setContentsMargins(0, 0, 0, 0)
        self.DirectoryOutputLayout.setSpacing(10)

        self.DirectoryOutputFrame = qtw.QFrame()
        self.DirectoryOutputFrame.setLayout(self.DirectoryOutputLayout)

        self.DirectoryOutputLabelLayout = qtw.QHBoxLayout()
        self.DirectoryOutputLabelLayout.setContentsMargins(0, 0, 0, 0)
        self.DirectoryOutputLabelLayout.setSpacing(5)

        self.DirectoryOutputLabelFrame = qtw.QFrame()
        self.DirectoryOutputLabelFrame.setLayout(self.DirectoryOutputLabelLayout)

        self.DirectoryOutputLabelLayout.addWidget(self.DirectoryOutputIcon)
        self.DirectoryOutputLabelLayout.addWidget(self.DirectoryOutputLabel)
        self.DirectoryOutputLabelLayout.addStretch()

        self.DirectoryOutputLayout.addWidget(self.DirectoryOutputLabelFrame)
        self.DirectoryOutputLayout.addWidget(self.DirectoryOutput)
        self.DirectoryOutputLayout.addStretch()

        self.ConvertButton = qtw.QPushButton("Convert to Base64")
        self.ConvertButton.setObjectName("ConvertButton")
        self.ConvertButton.setIcon(qtg.QIcon("Assets/codeIcon.png"))
        self.ConvertButton.setIconSize(qtc.QSize(20, 20))
        self.ConvertButton.setCursor(qtc.Qt.CursorShape.PointingHandCursor)

        self.InputsLayout.addWidget(self.DirectoryInputFrame)
        self.InputsLayout.addWidget(self.FileTypeComboFrame)
        self.InputsLayout.addWidget(self.DirectoryOutputFrame)
        self.InputsLayout.addWidget(self.ConvertButton)

        self.BodyLayout.addWidget(self.InputsFrame)

    def setFeedbackFrame(self):
        self.FeedbackLayout = qtw.QHBoxLayout()
        self.FeedbackLayout.setAlignment(qtc.Qt.AlignmentFlag.AlignLeft)
        self.FeedbackLayout.setContentsMargins(0, 0, 0, 0)
        self.FeedbackLayout.setSpacing(5)

        self.FeedbackFrame = qtw.QFrame()
        self.FeedbackFrame.setObjectName("FeedbackFrame")
        self.FeedbackFrame.setLayout(self.FeedbackLayout)
        self.FeedbackFrame.hide()

        self.FeedbackIcon = qtw.QLabel()

        self.FeedbackPixmap = qtg.QPixmap("Assets/errorIcon.png")
        self.FeedbackPixmapScaled = self.FeedbackPixmap.scaled(
            20,
            20,
            qtc.Qt.AspectRatioMode.KeepAspectRatio,
            qtc.Qt.TransformationMode.SmoothTransformation,
        )

        self.FeedbackIcon.setPixmap(self.FeedbackPixmapScaled)

        self.FeedbackLabel = qtw.QLabel()
        self.FeedbackLabel.setObjectName("FeedbackLabel")

        self.FeedbackLayout.addWidget(self.FeedbackIcon)
        self.FeedbackLayout.addWidget(self.FeedbackLabel)

        self.BodyLayout.addWidget(self.FeedbackFrame)

    def setInfoFrame(self):
        self.InfoLayout = qtw.QVBoxLayout()
        self.InfoLayout.setContentsMargins(0, 0, 0, 0)
        self.InfoLayout.setSpacing(0)

        self.InfoFrame = qtw.QFrame()
        self.InfoFrame.setObjectName("InfoFrame")
        self.InfoFrame.setLayout(self.InfoLayout)

        self.InfoLabel = qtw.QLabel()
        self.InfoLabel.setObjectName("InfoLabel")

        self.InfoHtmlText = """
        <style>
            h2{
                margin-bottom: 8px;
            }
            ul {
                color: #94a3b8;
                font-size: 13px;
                margin-left: -30px;
            }
            li {
                margin-bottom: 6px;
            }

            
        </style>
            <h2>How it works: </h2>
            <ul>
                <li>Scans the input directory for images of the specified type.<br>
                <strong>Notice: Scanning process happens on directory and its sub-directories</strong></li>
                <li>Converts each image to base64 encoding.</li>
                <li>Generates a Python file with all base64 strings.</li>
                <li>Saves the output file to your specified directory.</li>
            </ul>
        """
        self.InfoLabel.setText(self.InfoHtmlText)
        self.InfoLabel.setWordWrap(True)

        self.InfoLayout.addWidget(self.InfoLabel)

        self.BodyLayout.addWidget(self.InfoFrame)

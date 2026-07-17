app_styles = """
QMainWindow{
    background-color: #1e293b;
}

QFrame#HeaderIconFrame{
    background-color: #2563eb;
    border-radius: 12px;
    padding: 8px;
}

QLabel#DirectoryInputLabel,#DirectoryOutputLabel,#FileTypeComboLabel,#HeaderInnerLabel,#HeaderInnerSecondaryLabel{
    font-weight: bold;
}

QLabel#HeaderInnerLabel{
    font-size: 24px;
    color: #fff;
}

QLabel#HeaderInnerSecondaryLabel{
    font-size: 12px;
    color: #94a3b8;
}

QLineEdit, QComboBox, QComboBox QAbstractItemView {
    background-color: #0f172a;
    border: 1px solid #475569;
}

QLineEdit{
    font-size: 14px;
}

QLineEdit, QComboBox{
    padding: 12px;
    border-radius: 8px;
}

QComboBox , QComboBox QAbstractItemView{
    font-size: 11pt;
}

QComboBox::drop-down{
    background: transparent;
    border: None;
}

QComboBox::down-arrow{
    image: url("Assets/downArrowIcon.png");
    width: 20px;
    height: 20px;
    padding-right: 8px;
}

QComboBox QAbstractItemView {
    outline: None;
    padding: 4px;
}

QComboBox QAbstractItemView::item{
    border-radius: 8px;
    padding-left: 8px;
}

QComboBox QAbstractItemView::item:hover{
    background-color: #3b82f6;
}

QLineEdit:focus, QComboBox:focus, QComboBox:on , QComboBox:items{
    border-color: #3b82f6;
}

QLineEdit[state="DirectoryValid"]{
    border-color: green;
}
QLineEdit[state="DirectoryInvalid"]{
    border-color: red;
}


QPushButton#ConvertButton{
    background: #2563eb;
    padding: 14px;
    border-radius: 8px;
    text-align: center;
    font-size: 16px;
    font-weight: bold;
}
QPushButton#ConvertButton:hover{
    background: #1d4ed8;
}

QFrame#InfoFrame{
    background-color: #0f172a;
    padding: 12px;
    border-radius: 8px;
}

QFrame#FeedbackFrame{
    background-color: #450a0a;
    border: 1px solid #991b1b;
    border-radius: 8px;
    padding: 12px;
}

QFrame#FeedbackFrame[state="error"]{
    background-color: #450a0a;
    border-color: #991b1b;
}
QFrame#FeedbackFrame[state="success"]{
    background-color: #052e16;
    border-color: #166534;
}

QLabel#FeedbackLabel{
    font-size: 16px;
}



"""
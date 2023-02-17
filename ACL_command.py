import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QLineEdit

class MainWindow(QMainWindow):
    """main window class"""
    def __init__(self):
        """constructor"""
        super(MainWindow, self).__init__()
        self.setFixedSize(650, 350)
        self.setWindowTitle("ACL command generator")
        self.command = []
        self.label = QLabel("")
        self.label.setWordWrap(True)

        self.den_prem = QComboBox()
        self.den_prem.addItems(["Action", "deny", "permit", "delete", "list", "move"])
        self.den_prem.currentTextChanged.connect(self.text_changed)

        self.protocol = QComboBox()
        self.protocol.addItems(["Protocol", "ahp", "eigrp", "esp", "gre", "icmp", "ip", "ospf", "tcp", "udp"])
        self.protocol.currentTextChanged.connect(self.text_changed)

        self.source = QLineEdit()
        self.source.setPlaceholderText("Enter source IP and wild mask/line to delete")
        self.source.textChanged.connect(self.label.setText)
        self.add_source = QPushButton("Add")
        self.add_source.setCheckable(True)
        self.add_source.clicked.connect(self.add_ip)

        self.port_s = QComboBox()
        self.port_s.addItems(["<>=", "any", "eq", "gt", "lt", "neq", "range"])
        self.port_s.currentTextChanged.connect(self.text_changed)

        self.port_s2 = QComboBox()
        self.port_s2.addItems(["<>=", "eq", "gt", "lt", "neq", "range"])
        self.port_s2.currentTextChanged.connect(self.text_changed)

        self.port = QLineEdit()
        self.port.setPlaceholderText("Enter source port number")
        self.port.textChanged.connect(self.label.setText)
        self.add_port = QPushButton("Add")
        self.add_port.setCheckable(True)
        self.add_port.clicked.connect(self.add_portn)

        self.dist = QLineEdit()
        self.dist.setPlaceholderText("Enter dist IP and wild mask")
        self.dist.textChanged.connect(self.label.setText)
        self.add_dist = QPushButton("Add")
        self.add_dist.setCheckable(True)
        self.add_dist.clicked.connect(self.add_distn)

        self.port2 = QLineEdit()
        self.port2.setPlaceholderText("Enter dist port number")
        self.port2.textChanged.connect(self.label.setText)
        self.add_port2 = QPushButton("Add")
        self.add_port2.setCheckable(True)
        self.add_port2.clicked.connect(self.add_portn2)

        self.submit_button = QPushButton("Generate")
        self.submit_button.setCheckable(True)
        self.submit_button.clicked.connect(self.generate)

        self.command_line = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(self.den_prem)
        layout.addWidget(self.protocol)
        layout.addWidget(self.source, 2, 0, 1, 8)
        layout.addWidget(self.add_source, 2, 8)
        layout.addWidget(self.port_s, 3, 0)
        layout.addWidget(self.port, 3, 1, 1, 7 )
        layout.addWidget(self.add_port, 3, 8)
        layout.addWidget(self.dist, 4, 0, 1, 8)
        layout.addWidget(self.add_dist, 4, 8)
        layout.addWidget(self.port_s2, 5, 0)
        layout.addWidget(self.port2, 5, 1, 1, 7)
        layout.addWidget(self.add_port2, 5, 8)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.command_line, 7, 0, 1, 8)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def text_changed(self, s):
        self.command.append(s)
    def add_ip(self):
        self.command.append(self.source.text())
    def add_portn(self):
        self.command.append(self.port.text())
    def add_portn2(self):
        self.command.append(self.port2.text())
    def generate(self):
        a = (" ".join(self.command))
        self.command_line.setText(a)
        print(a)

    def add_distn(self):
        self.command.append(self.dist.text())
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
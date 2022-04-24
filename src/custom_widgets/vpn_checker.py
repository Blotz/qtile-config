from libqtile.widget import base
import subprocess


class ConnectionStatus(base.ThreadPoolText):
    """A simple widget to display if a given Vconnection is launched or not.
    This widget uses (so: needs) network manager's nmcli tool.
    A classic (and default) use case is to check if a vpn is ON or OFF and
    display a corresponding lock icon.
    setup the 'name' option to parse the output of the nmcli command.
    """

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("update_interval", 30, "Update time in seconds."),
        ("name", 'vpn', "name"),
        ("color_ok", "55cc55", "color_ok"),
        ("color_nok", "cc5555", "color_nok"),
        ("fmt_ok", "\U0001F510", "fmt_ok"),
        ("fmt_nok", "\U0001F513", "fmt_nok"),
    ]

    def __init__(self, **config):
        """Initalise VpnStatus widget."""
        base._TextBox.__init__(self, **config)
        self.add_defaults(ConnectionStatus.defaults)
        self.last_output = ''

    def poll(self):
        """Use nmcli to poll connexion status."""
        args = "systemctl is-active openvpn-client@%s.service" % self.name
        p1 = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
        # p2 = subprocess.Popen(["grep", self.name],
        #                       stdin=p1.stdout, stdout=subprocess.PIPE)
        # p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
        stdout, stderr = p1.communicate()
        if p1.returncode == 0:
            # ok we can find a connection
            self.last_output = stdout.decode('utf-8')
            self.layout.colour = "55cc55"
            return(self.fmt_ok)
        else:
            self.last_output = ''
            self.layout.colour = "cc5555"
            return(self.fmt_nok)

    def button_press(self, x, y, button):
        """handle mouse button press on the widget."""
        if button == 1:  # left click
            if self.last_output == "active":
                # Turn off vpn
                subprocess.call(
                '/usr/bin/notify-send -u low -t 1000 -a ConnectionStatus '
                '-c info "connected to: %s"' % self.name, shell=True)
            elif self.last_output == "inactive":
                # Turn on vpn
                subprocess.call(
                '/usr/bin/notify-send -u low -t 1000 -a ConnectionStatus '
                '-c info "disconnected to: %s"' % self.name, shell=True)
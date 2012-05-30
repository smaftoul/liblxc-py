import liblxc
import ctypes

LXC_LOG_PRIORITY=0
logs = liblxc.lxc_log_init("/tmp/lxc.log", LXC_LOG_PRIORITY, "", 0)

liblxc.lxc_caps_init()

conf = liblxc.lxc_conf_init()
liblxc.lxc_config_read("/var/lib/lxc/debian/config", conf)

container_argv = ((ctypes.c_char_p * 20) * 20)()
container_argv[0][0] = ctypes.c_char_p('/sbin/init')
container_argv[1][0] = ctypes.c_char_p('\0')

liblxc.lxc_start("debian", container_argv, conf)

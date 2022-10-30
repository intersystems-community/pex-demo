def log(pex_obj, msg):
    package_class_name = str(pex_obj.__class__).split("'")[1]
    class_name = package_class_name.split(".")[-1]
    pex_obj.LOGINFO("[%s] %s" % (class_name, msg))
    return
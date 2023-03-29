from mysql.connector import MySQLConnection

temp_username = None
temp_admin_uid = None

temp_current_selected_table = ""
temp_table_widget = None
temp_update_catalog_uid = None
temp_update_admin_uid = None
temp_update_order_uid = None
temp_update_reader_uid = None

temp_host_name = 'localhost'
temp_host_username = 'root'
temp_host_password = ''
temp_host_database = 'library'

conn = MySQLConnection(host=temp_host_name, user=temp_host_username, password=temp_host_password, database=temp_host_database)
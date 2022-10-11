from tkinter import *
import pyodbc
from tkinter import ttk

WIDTH = 1068
HEIGHT = 838

#Function that executes when log in button is clicked
def login():
    un = username_entry.get()
    pw = pw_entry.get()
    cursor = conn.cursor()
    query = f"SELECT * FROM system_users WHERE username='{un}' AND password='{pw}'"
    cursor.execute(query)
    results = cursor.fetchone()
    
    if results:
        is_admin = results[3]
        if is_admin:
            print("User found!" + str(results) )
            #The lift method brings the admin page to the front, it will not be visible until a successful login occurs
            admin_logged_in.lift()
            un_admin_text.set(f"Welcome, {un}!")
        else:
            print("User found!" + str(results) )
            user_logged_in.lift()
            un_user_text.set(f"Welcome, {un}!")
    else:
        invalid_login = Label(login_container, fg='red', text="INVALID USER CREDENTIALS", font=('Helvetica 10 bold'))
        invalid_login.grid(row=4, columnspan=2)


#Function that executes when logout button is clicked
def logout_clicked():
    admin_logged_in.lower()
    user_logged_in.lower()
    username_entry.delete(0, last='end')
    pw_entry.delete(0, last='end')

#function that executes when add new store is clicked
def add_store():
    add_store_data.lift()

#function that executes when submit is clicked on add new store frame
def submit_new_store():
    state_id = state_id_entry.get()
    city = city_entry.get()
    address = address_entry.get()
    cursor = conn.cursor()
    query = f"INSERT INTO blockhouse_stores (state_id, city, address) VALUES ({int(state_id)}, '{city}', '{address}')"
    cursor.execute(query)
    update_stores()
    entry_frame_cover.lift()

#function that executes when edit selected store button is clicked 
def edit_store():
    if store_tree.focus():
        edit_store_data.lift()
        selected_store = store_tree.item(store_tree.focus())
        values = selected_store['values']
        store_id_text.set(values[0])
        state_id_entry_update.delete(0, last='end')
        state_id_entry_update.insert(0, str(values[1]))
        city_entry_update.delete(0, last='end')
        city_entry_update.insert(0, values[2])
        address_entry_update.delete(0, last='end')
        address_entry_update.insert(0, values[3])


    # values = store_tree.item(selected_store)

#function that executes when submit is clicked on update store frame
def update_store():
    if store_tree.focus():
        store_id = int(store_id_label2.cget("text"))
        state_id = int(state_id_entry_update.get())
        city = city_entry_update.get()
        address = address_entry_update.get()
        cursor = conn.cursor()
        query = f"UPDATE blockhouse_stores SET state_id = {state_id}, city = '{city}', address = '{address}' WHERE store_id = {store_id}"
        cursor.execute(query)
        update_stores()
        entry_frame_cover.lift()


#function to update store list in the store treeview
def update_stores():
    store_tree.delete(*store_tree.get_children())
    cursor = conn.cursor()
    query = f"SELECT * FROM blockhouse_stores"
    cursor.execute(query)
    stores = cursor.fetchall()
    for store in stores:
        store_tree.insert("", index="end", values=(store[0], store[1], store[2], store[3]))
        store_info = f"{store[0]}"
        if store_info not in all_stores:
            all_stores.append(store_info)
            stores_with_all.append(store_info)

#function to update user list in the system users treeview
def update_users():
    users_tree.delete(*users_tree.get_children())
    cursor = conn.cursor()
    query = "SELECT * FROM system_users"
    cursor.execute(query)
    users = cursor.fetchall()
    for user in users:
        users_tree.insert("", index="end", values=(user[0], user[1], user[3]))

def update_suppliers():
    suppliers_tree.delete(*suppliers_tree.get_children())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM suppliers")
    suppliers = cursor.fetchall()
    for supplier in suppliers:
        suppliers_tree.insert("", index=END, values=(supplier[0], supplier[1], supplier[2], supplier[3], supplier[4], supplier[5]))
        sup_info = supplier[0]
        if sup_info not in all_sups:
            all_sups.append(sup_info)
            sups.append(sup_info)

def manage_products_clicked():
    products_main_frame.lift()

def cb_product_selected(event):
    selection = products_cb.get()
    products_tree.delete(*products_tree.get_children())
    cursor = conn.cursor()
    product_bottom_container.lift()
    details_form_cover.lift()
    if selection == "Bread":
        query = "SELECT * FROM suppliers_bread_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Cleaning":
        query = "SELECT * FROM suppliers_cleaning_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Coffee":
        query = "SELECT * FROM suppliers_coffee_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Dairy":
        query = "SELECT * FROM suppliers_dairy_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Meat":
        query = "SELECT * FROM suppliers_meat_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Other":
        query = "SELECT * FROM suppliers_other_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Paper":
        query = "SELECT * FROM suppliers_paper_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Produce":
        query = "SELECT * FROM suppliers_produce_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Retail":
        query = "SELECT * FROM suppliers_retail_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Sugars, Spices, Seasonings":
        query = "SELECT * FROM suppliers_sss_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))

def add_product_clicked():
    new_product_details_form.lift()
    supplier_id_entry_new.delete(0, END)
    product_name_entry_new.delete(0, END)
    manufacturer_entry_new.delete(0, END)
    ppc_entry_new.delete(0, END)
    case_qty_entry_new.delete(0, END)


def edit_product_clicked():
    if products_tree.focus():
        edit_product_details_form.lift()
        selected_product = products_tree.item(products_tree.focus())
        values = selected_product['values']
        product_id_text.set(values[0])
        supplier_id_entry.delete(0, last='end')
        supplier_id_entry.insert(0, str(values[1]))
        product_name_entry.delete(0, last='end')
        product_name_entry.insert(0, str(values[2]))
        manufacturer_entry.delete(0, last='end')
        manufacturer_entry.insert(0, str(values[3]))
        ppc_entry.delete(0, last='end')
        ppc_entry.insert(0, str(values[4]))
        case_qty_entry.delete(0, last='end')
        case_qty_entry.insert(0, str(values[5]))
        
        

def submit_new_product():
    selection = products_cb.get()
    sup_id = int(supplier_id_entry_new.get())
    prod_name = product_name_entry_new.get()
    man = manufacturer_entry_new.get()
    ppc = float(ppc_entry_new.get())
    case_qty = case_qty_entry_new.get()
    cursor = conn.cursor()
    if selection == "Bread":
        query = f"INSERT INTO suppliers_bread_products (supplier_id, product_name, manufacturer, price_per_case, case_qty) VALUES ({sup_id}, '{prod_name}', '{man}', {ppc}, '{case_qty}')"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_bread_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
        
    if selection == "Cleaning":
        query = f"INSERT INTO suppliers_cleaning_products (supplier_id, product_name, manufacturer, price_per_case, case_qty) VALUES ({sup_id}, '{prod_name}', '{man}', {ppc}, '{case_qty}')"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_cleaning_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
        
    if selection == "Coffee":
        query = f"INSERT INTO suppliers_coffee_products (supplier_id, product_name, manufacturer, price_per_case, case_qty) VALUES ({sup_id}, '{prod_name}', '{man}', {ppc}, '{case_qty}')"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_coffee_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
       
    if selection == "Dairy":
        query = f"INSERT INTO suppliers_dairy_products (supplier_id, product_name, manufacturer, price_per_case, case_qty) VALUES ({sup_id}, '{prod_name}', '{man}', {ppc}, '{case_qty}')"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_dairy_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
        
    if selection == "Meat":
        query = f"INSERT INTO suppliers_meat_products (supplier_id, product_name, manufacturer, price_per_case, case_qty) VALUES ({sup_id}, '{prod_name}', '{man}', {ppc}, '{case_qty}')"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_meat_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
        
    if selection == "Other":
        query = f"INSERT INTO suppliers_other_products (supplier_id, product_name, manufacturer, price_per_case, case_qty) VALUES ({sup_id}, '{prod_name}', '{man}', {ppc}, '{case_qty}')"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_other_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
        
    if selection == "Paper":
        query = f"INSERT INTO suppliers_paper_products (supplier_id, product_name, manufacturer, price_per_case, case_qty) VALUES ({sup_id}, '{prod_name}', '{man}', {ppc}, '{case_qty}')"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_paper_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
        
    if selection == "Produce":
        query = f"INSERT INTO suppliers_produce_products (supplier_id, product_name, manufacturer, price_per_case, case_qty) VALUES ({sup_id}, '{prod_name}', '{man}', {ppc}, '{case_qty}')"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_produce_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
        
    if selection == "Retail":
        query = f"INSERT INTO suppliers_retail_products (supplier_id, product_name, manufacturer, price_per_case, case_qty) VALUES ({sup_id}, '{prod_name}', '{man}', {ppc}, '{case_qty}')"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_retail_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
        
    if selection == "Sugars, Spices, Seasonings":
        query = f"INSERT INTO suppliers_sss_products (supplier_id, product_name, manufacturer, price_per_case, case_qty) VALUES ({sup_id}, '{prod_name}', '{man}', {ppc}, '{case_qty}')"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_sss_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))

def edit_product_submit():
    selection = products_cb.get()
    product_id = int(product_id_label2.cget("text"))
    sup_id = int(supplier_id_entry.get())
    prod_name = product_name_entry.get()
    man = manufacturer_entry.get()
    ppc = float(ppc_entry.get())
    case_qty = case_qty_entry.get()
    cursor = conn.cursor()
    if selection == "Bread":
        query = f"UPDATE suppliers_bread_products SET supplier_id = {sup_id}, product_name = '{prod_name}', manufacturer = '{man}', price_per_case = {ppc}, case_qty= '{case_qty}' WHERE sup_bre_product_id = {product_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_bread_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Cleaning":
        query = f"UPDATE suppliers_cleaning_products SET supplier_id = {sup_id}, product_name = '{prod_name}', manufacturer = '{man}', price_per_case = {ppc}, case_qty= '{case_qty}' WHERE sup_cle_product_id = {product_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_cleaning_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Coffee":
        query = f"UPDATE suppliers_coffee_products SET supplier_id = {sup_id}, product_name = '{prod_name}', manufacturer = '{man}', price_per_case = {ppc}, case_qty= '{case_qty}' WHERE sup_cof_product_id = {product_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_coffee_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Dairy":
        query = f"UPDATE suppliers_dairy_products SET supplier_id = {sup_id}, product_name = '{prod_name}', manufacturer = '{man}', price_per_case = {ppc}, case_qty= '{case_qty}' WHERE sup_dai_product_id = {product_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_dairy_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))    
    if selection == "Meat":
        query = f"UPDATE suppliers_meat_products SET supplier_id = {sup_id}, product_name = '{prod_name}', manufacturer = '{man}', price_per_case = {ppc}, case_qty= '{case_qty}' WHERE sup_mea_product_id = {product_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_meat_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Other":
        query = f"UPDATE suppliers_other_products SET supplier_id = {sup_id}, product_name = '{prod_name}', manufacturer = '{man}', price_per_case = {ppc}, case_qty= '{case_qty}' WHERE sup_oth_product_id = {product_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_other_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Paper":
        query = f"UPDATE suppliers_paper_products SET supplier_id = {sup_id}, product_name = '{prod_name}', manufacturer = '{man}', price_per_case = {ppc}, case_qty= '{case_qty}' WHERE sup_pap_product_id = {product_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_paper_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Produce":
        query = f"UPDATE suppliers_produce_products SET supplier_id = {sup_id}, product_name = '{prod_name}', manufacturer = '{man}', price_per_case = {ppc}, case_qty= '{case_qty}' WHERE sup_pro_product_id = {product_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_produce_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Retail":
        query = f"UPDATE suppliers_retail_products SET supplier_id = {sup_id}, product_name = '{prod_name}', manufacturer = '{man}', price_per_case = {ppc}, case_qty= '{case_qty}' WHERE sup_ret_product_id = {product_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_retail_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Sugars, Spices, Seasonings":
        query = f"UPDATE suppliers_sss_products SET supplier_id = {sup_id}, product_name = '{prod_name}', manufacturer = '{man}', price_per_case = {ppc}, case_qty= '{case_qty}' WHERE sup_sss_product_id = {product_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_sss_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            column
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))

def delete_product_clicked():
    if products_tree.focus():
        confirm_delete_product.lift()

def confirm_delete_clicked():
    selection = products_cb.get()
    selected_product = products_tree.item(products_tree.focus())
    prod_id = int(selected_product['values'][0])
    cursor = conn.cursor()
    if selection == "Bread":
        query = f"DELETE FROM suppliers_bread_products WHERE sup_bre_product_id = {prod_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_bread_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Cleaning":
        query = f"DELETE FROM suppliers_cleaning_products WHERE sup_cle_product_id = {prod_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_cleaning_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Coffee":
        query = f"DELETE FROM suppliers_coffee_products WHERE sup_cof_product_id = {prod_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_coffee_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Dairy":
        query = f"DELETE FROM suppliers_dairy_products WHERE sup_dai_product_id = {prod_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_dairy_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Meat":
        query = f"DELETE FROM suppliers_meat_products WHERE sup_mea_product_id = {prod_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_meat_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Other":
        query = f"DELETE FROM suppliers_other_products WHERE sup_oth_product_id = {prod_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_other_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Paper":
        query = f"DELETE FROM suppliers_paper_products WHERE sup_pap_product_id = {prod_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_paper_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Produce":
        query = f"DELETE FROM suppliers_produce_products WHERE sup_pro_product_id = {prod_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_produce_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Retail":
        query = f"DELETE FROM suppliers_retail_products WHERE sup_ret_product_id = {prod_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_retail_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Sugars, Spices, Seasonings":
        query = f"DELETE FROM suppliers_sss_products WHERE sup_sss_product_id = {prod_id}"
        cursor.execute(query)
        details_form_cover.lift()
        query = "SELECT * FROM suppliers_sss_products"
        cursor.execute(query)
        products_tree.delete(*products_tree.get_children())
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))

def counts_clicked():
    counts_main_frame.lift()

def cb_store_selected(event):
    counts_header2.pack(pady=10)
    counts_products_cb.pack(fill='x')
    counts_svar.set("")
    
def cb_product_type_selected(event):
    counts_data.lift()
    prod = counts_products_cb.get()
    store_id = counts_cb.get()
    cursor = conn.cursor()
    counts_cb['state'] = DISABLED
    counts_products_cb['state'] = DISABLED
    global item_container
    item_container = Frame(counts_data, relief=SUNKEN, highlightbackground="black", highlightthickness=.5)
    mycan = Canvas(item_container, bg='white', highlightthickness=0, borderwidth=1)
    mycan.pack(side=LEFT, fill="both", expand="yes")
    counts_vsb = Scrollbar(item_container, orient=VERTICAL, command=mycan.yview)
    counts_vsb.pack(side='right', fill='y')
    mycan.config(yscrollcommand=counts_vsb.set)
    mycan.bind('<Configure>', lambda e: mycan.configure(scrollregion = mycan.bbox('all')))
    scrollable_frame = Frame(mycan, bg='white')
    mycan.create_window((0,0), window=scrollable_frame)
    item_container.place(relwidth=.46, relheight=.9, relx=.27, rely=.05)

    item_label = Label(scrollable_frame, text=prod, font=('Helvetica 12 bold'), bg='white')
    item_label.grid(row=0, column=0, columnspan=2, pady=10)
    item_name_label = Label(scrollable_frame, text="Product Name", font=('Helvetica 10 bold'), bg='white')
    item_name_label.grid(row=1, column=0)
    item_qty_label = Label(scrollable_frame, text="Current Case Quantity", font=('Helvetica 10 bold'), bg='white')
    item_qty_label.grid(row=1, column=1)
    row = 2
    entries = []
    if prod == "Bread":
        cursor.execute(f"SELECT * FROM full_store_inventory_report WHERE store_id={store_id} AND sto_bre_product_id IS NOT NULL")
        items = cursor.fetchall()
        for item in items:
            label = Label(scrollable_frame, bg='white', text=item[11], font=('Arial 9'), padx=10)
            label.grid(row=row, column=0, sticky='w', padx=5, pady=10)
            entry = Entry(scrollable_frame, font=('Arial 9'))
            entry.insert(0, item[12])
            entry.grid(row=row, column=1, sticky='w', padx=5, pady=10)
            row += 1
            entries.append(entry)
        submit_counts_button = Button(scrollable_frame, text="Submit", font=('Arial 10'), command=lambda arg1=store_id, arg2=prod, arg3=entries: submit_counts(arg1, arg2, arg3))
        submit_counts_button.grid(row=row, column=0, pady=10)
        cancel_counts_button = Button(scrollable_frame, text="Cancel", font=('Arial 10'), command=lambda: [item_container.destroy(), counts_svar.set(""), change_count_cb_state() ])
        cancel_counts_button.grid(row=row, column=1, pady=10)
    if prod == "Cleaning":
        cursor.execute(f"SELECT * FROM full_store_inventory_report WHERE store_id={store_id} AND sto_cle_product_id IS NOT NULL")
        items = cursor.fetchall()
        for item in items:
            label = Label(scrollable_frame, bg='white', text=item[11], font=('Arial 9'), padx=10)
            label.grid(row=row, column=0, sticky='w', padx=5, pady=10)
            entry = Entry(scrollable_frame, font=('Arial 9'))
            entry.insert(0, item[12])
            entry.grid(row=row, column=1, sticky='w', padx=5, pady=10)
            row += 1
            entries.append(entry)
        submit_counts_button = Button(scrollable_frame, text="Submit", font=('Arial 10'), command=lambda arg1=store_id, arg2=prod, arg3=entries: submit_counts(arg1, arg2, arg3))
        submit_counts_button.grid(row=row, column=0, pady=10)
        cancel_counts_button = Button(scrollable_frame, text="Cancel", font=('Arial 10'), command=lambda: [item_container.destroy(), counts_svar.set(""), change_count_cb_state() ])
        cancel_counts_button.grid(row=row, column=1, pady=10)
    if prod == "Coffee":
        cursor.execute(f"SELECT * FROM full_store_inventory_report WHERE store_id={store_id} AND sto_cof_product_id IS NOT NULL")
        items = cursor.fetchall()
        for item in items:
            label = Label(scrollable_frame, bg='white', text=item[11], font=('Arial 9'), padx=10)
            label.grid(row=row, column=0, sticky='w', padx=5, pady=10)
            entry = Entry(scrollable_frame, font=('Arial 9'))
            entry.insert(0, item[12])
            entry.grid(row=row, column=1, sticky='w', padx=5, pady=10)
            row += 1
            entries.append(entry)
        submit_counts_button = Button(scrollable_frame, text="Submit", font=('Arial 10'), command=lambda arg1=store_id, arg2=prod, arg3=entries: submit_counts(arg1, arg2, arg3))
        submit_counts_button.grid(row=row, column=0, pady=10)
        cancel_counts_button = Button(scrollable_frame, text="Cancel", font=('Arial 10'), command=lambda: [item_container.destroy(), counts_svar.set(""), change_count_cb_state() ])
        cancel_counts_button.grid(row=row, column=1, pady=10)
    if prod == "Dairy":
        cursor.execute(f"SELECT * FROM full_store_inventory_report WHERE store_id={store_id} AND sto_dai_product_id IS NOT NULL")
        items = cursor.fetchall()
        for item in items:
            label = Label(scrollable_frame, bg='white', text=item[11], font=('Arial 9'), padx=10)
            label.grid(row=row, column=0, sticky='w', padx=5, pady=10)
            entry = Entry(scrollable_frame, font=('Arial 9'))
            entry.insert(0, item[12])
            entry.grid(row=row, column=1, sticky='w', padx=5, pady=10)
            row += 1
            entries.append(entry)
        submit_counts_button = Button(scrollable_frame, text="Submit", font=('Arial 10'), command=lambda arg1=store_id, arg2=prod, arg3=entries: submit_counts(arg1, arg2, arg3))
        submit_counts_button.grid(row=row, column=0, pady=10)
        cancel_counts_button = Button(scrollable_frame, text="Cancel", font=('Arial 10'), command=lambda: [item_container.destroy(), counts_svar.set(""), change_count_cb_state() ])
        cancel_counts_button.grid(row=row, column=1, pady=10)
    if prod == "Meat":
        cursor.execute(f"SELECT * FROM full_store_inventory_report WHERE store_id={store_id} AND sto_meat_product_id IS NOT NULL")
        items = cursor.fetchall()
        for item in items:
            label = Label(scrollable_frame, bg='white', text=item[11], font=('Arial 9'), padx=10)
            label.grid(row=row, column=0, sticky='w', padx=5, pady=10)
            entry = Entry(scrollable_frame, font=('Arial 9'))
            entry.insert(0, item[12])
            entry.grid(row=row, column=1, sticky='w', padx=5, pady=10)
            row += 1
            entries.append(entry)
        submit_counts_button = Button(scrollable_frame, text="Submit", font=('Arial 10'), command=lambda arg1=store_id, arg2=prod, arg3=entries: submit_counts(arg1, arg2, arg3))
        submit_counts_button.grid(row=row, column=0, pady=10)
        cancel_counts_button = Button(scrollable_frame, text="Cancel", font=('Arial 10'), command=lambda: [item_container.destroy(), counts_svar.set(""), change_count_cb_state() ])
        cancel_counts_button.grid(row=row, column=1, pady=10)
    if prod == "Other":
        cursor.execute(f"SELECT * FROM full_store_inventory_report WHERE store_id={store_id} AND sto_oth_product_id IS NOT NULL")
        items = cursor.fetchall()
        for item in items:
            label = Label(scrollable_frame, bg='white', text=item[11], font=('Arial 9'), padx=10)
            label.grid(row=row, column=0, sticky='w', padx=5, pady=10)
            entry = Entry(scrollable_frame, font=('Arial 9'))
            entry.insert(0, item[12])
            entry.grid(row=row, column=1, sticky='w', padx=5, pady=10)
            row += 1
            entries.append(entry)
        submit_counts_button = Button(scrollable_frame, text="Submit", font=('Arial 10'), command=lambda arg1=store_id, arg2=prod, arg3=entries: submit_counts(arg1, arg2, arg3))
        submit_counts_button.grid(row=row, column=0, pady=10)
        cancel_counts_button = Button(scrollable_frame, text="Cancel", font=('Arial 10'), command=lambda: [item_container.destroy(), counts_svar.set(""), change_count_cb_state() ])
        cancel_counts_button.grid(row=row, column=1, pady=10)
    if prod == "Paper":
        cursor.execute(f"SELECT * FROM full_store_inventory_report WHERE store_id={store_id} AND sto_pap_product_id IS NOT NULL")
        items = cursor.fetchall()
        for item in items:
            label = Label(scrollable_frame, bg='white', text=item[11], font=('Arial 9'), padx=10)
            label.grid(row=row, column=0, sticky='w', padx=5, pady=10)
            entry = Entry(scrollable_frame, font=('Arial 9'))
            entry.insert(0, item[12])
            entry.grid(row=row, column=1, sticky='w', padx=5, pady=10)
            row += 1
            entries.append(entry)
        submit_counts_button = Button(scrollable_frame, text="Submit", font=('Arial 10'), command=lambda arg1=store_id, arg2=prod, arg3=entries: submit_counts(arg1, arg2, arg3))
        submit_counts_button.grid(row=row, column=0, pady=10)
        cancel_counts_button = Button(scrollable_frame, text="Cancel", font=('Arial 10'), command=lambda: [item_container.destroy(), counts_svar.set(""), change_count_cb_state() ])
        cancel_counts_button.grid(row=row, column=1, pady=10)
    if prod == "Produce":
        cursor.execute(f"SELECT * FROM full_store_inventory_report WHERE store_id={store_id} AND sto_pro_product_id IS NOT NULL")
        items = cursor.fetchall()
        for item in items:
            label = Label(scrollable_frame, bg='white', text=item[11], font=('Arial 9'), padx=10)
            label.grid(row=row, column=0, sticky='w', padx=5, pady=10)
            entry = Entry(scrollable_frame, font=('Arial 9'))
            entry.insert(0, item[12])
            entry.grid(row=row, column=1, sticky='w', padx=5, pady=10)
            row += 1
            entries.append(entry)
        submit_counts_button = Button(scrollable_frame, text="Submit", font=('Arial 10'), command=lambda arg1=store_id, arg2=prod, arg3=entries: submit_counts(arg1, arg2, arg3))
        submit_counts_button.grid(row=row, column=0, pady=10)
        cancel_counts_button = Button(scrollable_frame, text="Cancel", font=('Arial 10'), command=lambda: [item_container.destroy(), counts_svar.set(""), change_count_cb_state() ])
        cancel_counts_button.grid(row=row, column=1, pady=10)
    if prod == "Retail":
        cursor.execute(f"SELECT * FROM full_store_inventory_report WHERE store_id={store_id} AND sto_ret_product_id IS NOT NULL")
        items = cursor.fetchall()
        for item in items:
            label = Label(scrollable_frame, bg='white', text=item[11], font=('Arial 9'), padx=10)
            label.grid(row=row, column=0, sticky='w', padx=5, pady=10)
            entry = Entry(scrollable_frame, font=('Arial 9'))
            entry.insert(0, item[12])
            entry.grid(row=row, column=1, sticky='w', padx=5, pady=10)
            row += 1
            entries.append(entry)
        submit_counts_button = Button(scrollable_frame, text="Submit", font=('Arial 10'), command=lambda arg1=store_id, arg2=prod, arg3=entries: submit_counts(arg1, arg2, arg3))
        submit_counts_button.grid(row=row, column=0, pady=10)
        cancel_counts_button = Button(scrollable_frame, text="Cancel", font=('Arial 10'), command=lambda: [item_container.destroy(), counts_svar.set(""), change_count_cb_state() ])
        cancel_counts_button.grid(row=row, column=1, pady=10)
    if prod == "Sugars, Spices, Seasonings":
        cursor.execute(f"SELECT * FROM full_store_inventory_report WHERE store_id={store_id} AND sto_sss_product_id IS NOT NULL")
        items = cursor.fetchall()
        for item in items:
            label = Label(scrollable_frame, bg='white', text=item[11], font=('Arial 9'), padx=10)
            label.grid(row=row, column=0, sticky='w', padx=5, pady=10)
            entry = Entry(scrollable_frame, font=('Arial 9'))
            entry.insert(0, item[12])
            entry.grid(row=row, column=1, sticky='w', padx=5, pady=10)
            row += 1
            entries.append(entry)
        submit_counts_button = Button(scrollable_frame, text="Submit", font=('Arial 10'), command=lambda arg1=store_id, arg2=prod, arg3=entries: submit_counts(arg1, arg2, arg3))
        submit_counts_button.grid(row=row, column=0, pady=10)
        cancel_counts_button = Button(scrollable_frame, text="Cancel", font=('Arial 10'), command=lambda: [item_container.destroy(), counts_svar.set(""), change_count_cb_state() ])
        cancel_counts_button.grid(row=row, column=1, pady=10)
    mycan.update_idletasks()
    mycan.yview_moveto(0)
    

def change_count_cb_state():
    if (counts_cb['state'] == READABLE):
        counts_cb['state'] = DISABLED
        counts_products_cb['state'] = DISABLED
    else:
        counts_cb['state'] = READABLE
        counts_products_cb['state'] = READABLE




def submit_counts(sto_id, prod, counts):
    cursor = conn.cursor()
    if prod == "Bread":
        i = 1
        for count in counts:
            cursor.execute(f"UPDATE store_bread_qty SET current_case_qty = {count.get()} WHERE store_id = {sto_id} AND sup_bre_product_id = {i}")
            i += 1
        item_container.destroy()
    if prod == "Cleaning":
        i = 1
        for count in counts:
            cursor.execute(f"UPDATE store_cleaning_qty SET current_case_qty = {count.get()} WHERE store_id = {sto_id} AND sup_cle_product_id = {i}")
            i += 1
        item_container.destroy()
    if prod == "Coffee":
        i = 1
        for count in counts:
            cursor.execute(f"UPDATE store_coffee_qty SET current_case_qty = {count.get()} WHERE store_id = {sto_id} AND sup_cof_product_id = {i}")
            i += 1
        item_container.destroy()
    if prod == "Dairy":
        i = 1
        for count in counts:
            cursor.execute(f"UPDATE store_dairy_qty SET current_case_qty = {count.get()} WHERE store_id = {sto_id} AND sup_dai_product_id = {i}")
            i += 1
        item_container.destroy()
    if prod == "Meat":
        i = 1
        for count in counts:
            cursor.execute(f"UPDATE store_meat_qty SET current_case_qty = {count.get()} WHERE store_id = {sto_id} AND sup_mea_product_id = {i}")
            i += 1
        item_container.destroy()
    if prod == "Other":
        i = 1
        for count in counts:
            cursor.execute(f"UPDATE store_other_qty SET current_case_qty = {count.get()} WHERE store_id = {sto_id} AND sup_oth_product_id = {i}")
            i += 1
        item_container.destroy()
    if prod == "Paper":
        i = 1
        for count in counts:
            cursor.execute(f"UPDATE store_paper_qty SET current_case_qty = {count.get()} WHERE store_id = {sto_id} AND sup_pap_product_id = {i}")
            i += 1
        item_container.destroy()
    if prod == "Produce":
        i = 1
        for count in counts:
            cursor.execute(f"UPDATE store_produce_qty SET current_case_qty = {count.get()} WHERE store_id = {sto_id} AND sup_pro_product_id = {i}")
            i += 1
        item_container.destroy()
    if prod == "Retail":
        i = 1
        for count in counts:
            cursor.execute(f"UPDATE store_retail_qty SET current_case_qty = {count.get()} WHERE store_id = {sto_id} AND sup_ret_product_id = {i}")
            i += 1
        item_container.destroy()
    if prod == "Sugars, Spices, Seasonings":
        i = 1
        for count in counts:
            cursor.execute(f"UPDATE store_sss_qty SET current_case_qty = {count.get()} WHERE store_id = {sto_id} AND sup_sss_product_id = {i}")
            i += 1
        item_container.destroy()
    
    counts_svar.set("")
    change_count_cb_state()

def manage_suppliers_clicked():
    suppliers_main_frame.lift()
    suppliers_data_frame_cover.lift()
    update_suppliers()

def add_new_supplier():
    new_supplier_entry.lift()
    new_supplier_name_entry.delete(0, END)
    new_supplier_phone_entry.delete(0, END)
    new_supplier_email_entry.delete(0, END)
    new_supplier_stateid_entry.delete(0, END)
    new_supplier_county_entry.delete(0, END)

def new_supplier_submitted():
    cursor = conn.cursor()
    sup_name = new_supplier_name_entry.get()
    sup_phone = new_supplier_phone_entry.get()
    sup_email = new_supplier_email_entry.get()
    sup_sid = new_supplier_stateid_entry.get()
    sup_county = new_supplier_county_entry.get()
    query = f"INSERT INTO suppliers (supplier_name, phone, email, state_id, county) VALUES ('{sup_name}', '{sup_phone}', '{sup_email}', {sup_sid}, '{sup_county}')"
    cursor.execute(query)
    update_suppliers()
    suppliers_data_frame_cover.lift()

def edit_supplier():
    if suppliers_tree.focus():
        edit_supplier_entry.lift()
        selection = suppliers_tree.item(suppliers_tree.focus())
        selected_supplier = selection['values']
        sup_id.set(selected_supplier[0])
        edit_supplier_name_entry.insert(0, selected_supplier[1])
        edit_supplier_phone_entry.insert(0, selected_supplier[2])
        edit_supplier_email_entry.insert(0, selected_supplier[3])
        edit_supplier_stateid_entry.insert(0, selected_supplier[4])
        edit_supplier_county_entry.insert(0, selected_supplier[5])

def edit_supplier_submitted():
    cursor = conn.cursor()
    sup_name = edit_supplier_name_entry.get()
    sup_phone = edit_supplier_phone_entry.get()
    sup_email = edit_supplier_email_entry.get()
    sup_sid = edit_supplier_stateid_entry.get()
    sup_county = edit_supplier_county_entry.get()
    s_id = edit_supplier_supid_label2.cget("text")
    query = f"UPDATE suppliers SET supplier_name = '{sup_name}', phone = '{sup_phone}', email = '{sup_email}', state_id = {sup_sid}, county = '{sup_county}' WHERE supplier_id = {s_id}"
    cursor.execute(query)
    update_suppliers()
    suppliers_data_frame_cover.lift()

def delete_supplier():
    error_label.pack_forget()
    if suppliers_tree.focus():
        delete_supplier_data.lift()

def confirm_supplier_delete_clicked():
        selection = suppliers_tree.item(suppliers_tree.focus())
        selected_supplier = selection['values']
        s_id = selected_supplier[0]
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM suppliers_other_products WHERE supplier_id = {s_id}")
        results = cursor.fetchall()
        if results:
            error_label.pack()

def view_orders_clicked():
    view_orders_main_frame.lift()

def view_invoices_clicked():
    invoices_main_frame.lift()

def view_cust_invoices():
    cust_invoices_main_frame.lift()

def delete_cancel_order_clicked():
    delete_order_main_frame.lift()      

def get_orders_clicked():
    orders_tree.delete(*orders_tree.get_children())
    orders_details_tree.delete(*orders_details_tree.get_children())
    edit_rec_date_entry.delete(0, END)
    edit_place_date_entry.delete(0, END)
    stoid = orders_stores_cb.get()
    supid = orders_sups_cb.get()
    received = order_var.get()
    cursor=conn.cursor()
    if received == 'both':
        if stoid == 'All Stores' and supid == 'All Suppliers':
            cursor.execute("SELECT * FROM orders")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    orders_tree.insert("", index="end", values=(order[0], order[1], order[2], order[3], order[4]))
        elif stoid == 'All Stores':
            cursor.execute(f"SELECT * FROM orders WHERE supplier_id = {supid}")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    orders_tree.insert("", index="end", values=(order[0], order[1], order[2], order[3], order[4]))
        elif supid == 'All Suppliers':
            cursor.execute(f"SELECT * FROM orders WHERE store_id = {stoid}")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    orders_tree.insert("", index="end", values=(order[0], order[1], order[2], order[3], order[4]))
        else:
            cursor.execute(f"SELECT * FROM orders WHERE store_id = {stoid} AND supplier_id = {supid}")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    orders_tree.insert("", index="end", values=(order[0], order[1], order[2], order[3], order[4]))
        
    if received == 'placed_and_received':
        if stoid == 'All Stores' and supid == 'All Suppliers':
            cursor.execute("SELECT * FROM orders WHERE received_date IS NOT NULL")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    orders_tree.insert("", index="end", values=(order[0], order[1], order[2], order[3], order[4]))
        elif stoid == 'All Stores':
            cursor.execute(f"SELECT * FROM orders WHERE supplier_id = {supid} AND received_date IS NOT NULL")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    orders_tree.insert("", index="end", values=(order[0], order[1], order[2], order[3], order[4]))
        elif supid == 'All Suppliers':
            cursor.execute(f"SELECT * FROM orders WHERE store_id = {stoid} AND received_date IS NOT NULL")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    orders_tree.insert("", index="end", values=(order[0], order[1], order[2], order[3], order[4]))
        else:
            cursor.execute(f"SELECT * FROM orders WHERE store_id = {stoid} AND supplier_id = {supid} AND received_date IS NOT NULL")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    orders_tree.insert("", index="end", values=(order[0], order[1], order[2], order[3], order[4]))

    if received == 'placed':
        if stoid == 'All Stores' and supid == 'All Suppliers':
            cursor.execute("SELECT * FROM orders WHERE received_date IS NULL")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    orders_tree.insert("", index="end", values=(order[0], order[1], order[2], order[3], order[4]))
        elif stoid == 'All Stores':
            cursor.execute(f"SELECT * FROM orders WHERE supplier_id = {supid} AND received_date IS NULL")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    orders_tree.insert("", index="end", values=(order[0], order[1], order[2], order[3], order[4]))
        elif supid == 'All Suppliers':
            cursor.execute(f"SELECT * FROM orders WHERE store_id = {stoid} AND received_date IS NULL")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    orders_tree.insert("", index="end", values=(order[0], order[1], order[2], order[3], order[4]))
        else:
            cursor.execute(f"SELECT * FROM orders WHERE store_id = {stoid} AND supplier_id = {supid} AND received_date IS NULL")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    orders_tree.insert("", index="end", values=(order[0], order[1], order[2], order[3], order[4]))

def order_selected(event):
    orders_details_tree.delete(*orders_details_tree.get_children())
    selected_order = orders_tree.item(orders_tree.focus())
    order_details = selected_order['values']
    order_id = order_details[0]
    date_placed = order_details[3]
    date_rec = order_details[4]
    # order_id = (selected_order['values'][0])
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM order_report WHERE order_id = {order_id}")
    order_details = cursor.fetchall()
    grand_total = 0
    for item in order_details:
        cost = (item[2] * item[3])
        orders_details_tree.insert("", index="end", values=(item[1], item[2], item[3], round(cost, 2)))
        grand_total += cost
    orders_details_tree.insert("", index="end", values=("", "", "", ""))
    orders_details_tree.insert("", index="end", values=("", "", "", ""))    
    orders_details_tree.insert("", index="end", values=("GRAND TOTAL", "", "", round(grand_total, 2)))
    edit_rec_submit_button['state'] = 'normal'
    sv_dateplaced.set(date_placed)
    sv_daterec.set(date_rec)
    edit_place_date_entry.delete(0, END)
    edit_rec_date_entry.delete(0, END)
    edit_place_date_entry.insert(0, sv_dateplaced.get())
    edit_rec_date_entry.insert(0, sv_daterec.get())

def get_events_clicked():
    events_tree.delete(*events_tree.get_children())
    event_details_tree.delete(*event_details_tree.get_children())
    stoid = events_stores_cb.get()
    cid_svar.set("")
    cn_svar.set("")
    cp_svar.set("")
    ce_svar.set("")
    l_name = ""
    if events_cust_entry.get() != "":
        l_name = events_cust_entry.get()
    completed = event_var.get()
    cursor = conn.cursor()
    if completed == 'both':
        if stoid == 'All Stores' and l_name == "":
            q = "SELECT * FROM events_with_names ORDER BY first_name ASC"
            cursor.execute(q)
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    events_tree.insert("", index=END, values=(order[0], order[1].strip(), order[2].strip(), order[3], order[4]))
        elif stoid == 'All Stores':
            q = f"SELECT * FROM events_with_names WHERE last_name = '{l_name}' ORDER BY first_name ASC"
            cursor.execute(q)
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    events_tree.insert("", index=END, values=(order[0], order[1].strip(), order[2].strip(), order[3], order[4]))
        elif l_name == "":
            q = f"SELECT * FROM events_with_names WHERE store_id = {stoid} ORDER BY first_name ASC"
            cursor.execute(q)
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    events_tree.insert("", index=END, values=(order[0], order[1].strip(), order[2].strip(), order[3], order[4]))
        else:
            q = f"SELECT * FROM events_with_names WHERE store_id = {stoid} AND last_name = '{l_name}' ORDER BY first_name ASC"
            cursor.execute(q)
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    events_tree.insert("", index=END, values=(order[0], order[1].strip(), order[2].strip(), order[3], order[4]))
        
    if completed == 'past':
        if stoid == 'All Stores' and l_name == "":
            cursor.execute("SELECT * FROM events_with_names WHERE event_date < GETDATE() ORDER BY first_name ASC")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    events_tree.insert("", index=END, values=(order[0], order[1].strip(), order[2].strip(), order[3], order[4]))
        elif stoid == 'All Stores':
            cursor.execute(f"SELECT * FROM events_with_names WHERE last_name = '{l_name}' AND event_date < GETDATE() ORDER BY first_name ASC")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    events_tree.insert("", index=END, values=(order[0], order[1].strip(), order[2].strip(), order[3], order[4]))
        elif l_name == "":
            cursor.execute(f"SELECT * FROM events_with_names WHERE store_id = {stoid} AND event_date < GETDATE() ORDER BY first_name ASC")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    events_tree.insert("", index=END, values=(order[0], order[1].strip(), order[2].strip(), order[3], order[4]))
        else:
            cursor.execute(f"SELECT * FROM events_with_names WHERE store_id = {stoid} AND last_name = '{l_name}' AND event_date < GETDATE() ORDER BY first_name ASC")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    events_tree.insert("", index=END, values=(order[0], order[1].strip(), order[2].strip(), order[3], order[4]))

    if completed == 'future':
        if stoid == 'All Stores' and l_name == "":
            cursor.execute("SELECT * FROM events_with_names WHERE event_date > GETDATE() ORDER BY first_name ASC")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    events_tree.insert("", index=END, values=(order[0], order[1].strip(), order[2].strip(), order[3], order[4]))
        elif stoid == 'All Stores':
            cursor.execute(f"SELECT * FROM events_with_names WHERE last_name = '{l_name}' AND event_date > GETDATE() ORDER BY first_name ASC")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    events_tree.insert("", index=END, values=(order[0], order[1].strip(), order[2].strip(), order[3], order[4]))
        elif l_name == "":
            cursor.execute(f"SELECT * FROM events_with_names WHERE store_id = {stoid} AND event_date > GETDATE() ORDER BY first_name ASC")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    events_tree.insert("", index=END, values=(order[0], order[1].strip(), order[2].strip(), order[3], order[4]))
        else:
            cursor.execute(f"SELECT * FROM events_with_names WHERE store_id = {stoid} AND last_name = '{l_name}' AND event_date > GETDATE() ORDER BY first_name ASC")
            orders = cursor.fetchall()
            for order in orders:
                if order[5] != True:
                    events_tree.insert("", index=END, values=(order[0], order[1].strip(), order[2].strip(), order[3], order[4]))
    events_cust_entry.delete(0, END)
    
    
    

def event_selected(event):
    event_details_tree.delete(*event_details_tree.get_children())
    selected_event = events_tree.item(events_tree.focus())
    event_details = selected_event['values']
    event_id = event_details[0]
    fn = event_details[1]
    ln = event_details[2]
    # order_id = (selected_order['values'][0])
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM catering_event_report WHERE event_id = {event_id}")
    event_details = cursor.fetchall()
    grand_total = 0
    for item in event_details:
        cost = (item[4] * item[3])
        event_details_tree.insert("", index="end", values=(item[2], item[3], item[4], round(cost, 2)))
        grand_total += cost
    event_details_tree.insert("", index="end", values=("", "", "", ""))
    event_details_tree.insert("", index="end", values=("", "", "", ""))    
    event_details_tree.insert("", index="end", values=("GRAND TOTAL", "", "", round(grand_total, 2)))
    cursor.execute(f"SELECT * FROM events_with_names WHERE event_id = {event_id} ")
    cust = cursor.fetchone()
    full_name = cust[1].strip() + " " + cust[2].strip()
    cid_svar.set(cust[6])
    cn_svar.set(full_name)
    cp_svar.set(cust[8])
    ce_svar.set(cust[7])



def create_order_clicked():
    create_order_main_frame.lift()

def change_catering_states():
    if event_date_entry['state'] == 'normal':
        event_date_entry['state'] = 'disabled'
        catering_store_cb['state'] = 'disabled'
    else:
        event_date_entry['state'] = 'normal'
        catering_store_cb['state'] = 'normal'

def begin_event_clicked():
    if customer_list_tree.focus() and catering_store_cb.get() != "" and event_date_entry != "":
        catering_buttons_container.lift()
        change_catering_states()
        selected_customer = customer_list_tree.item(customer_list_tree.focus())
        customer = selected_customer['values'][0]
        customer_name = selected_customer['values'][1]
        store = catering_store_cb.get()
        event_date = event_date_entry.get()
        cursor = conn.cursor()
        customer_list_tree.delete(*customer_list_tree.get_children())
        cursor.execute(f"INSERT INTO catering_events (customer_id, store_id, event_date) VALUES ({customer}, {store}, '{event_date}')")
        print(f"INSERT INTO catering_events (customer_id, store_id, event_date) VALUES ({customer}, {store}, '{event_date}')")
        cursor.execute("SELECT event_id FROM catering_events WHERE event_id=(SELECT max(event_id) FROM catering_events);")
        result = cursor.fetchone()
        global gl_event_id
        gl_event_id = result[0]
        global menu_items_data_frame
        menu_items_data_frame = Frame(catering_menu_container, highlightbackground="grey", highlightthickness=.5)
        menucan = Canvas(menu_items_data_frame, highlightthickness=0)
        menucan.pack(side=LEFT, fill=BOTH, expand=YES)
        menu_vsb = Scrollbar(menu_items_data_frame, orient=VERTICAL, command=menucan.yview)
        menu_vsb.pack(side=RIGHT, fill=Y)
        menucan.config(yscrollcommand=menu_vsb.set)
        menucan.bind('<Configure>', lambda e: menucan.configure(scrollregion = menucan.bbox('all')))
        scrollable_menu = Frame(menucan, highlightthickness=0)
        menucan.create_window((0,0), window=scrollable_menu)
        menu_items_data_frame.place(relwidth=1, relheight=1)

        header_label = Label(scrollable_menu, text=f"Enter the menu items for {customer_name.rstrip(customer_name[-1])}'s event:", font=("Arial 12 bold"), pady=10)
        header_label.grid(row=0, column=0, columnspan=4)
        item_id_label = Label(scrollable_menu, text="Item ID", font=("Arial 10 bold"))
        item_id_label.grid(row=1, column=0, padx=20)
        item_name_label = Label(scrollable_menu, text="Item Name", font=("Arial 10 bold"))
        item_name_label.grid(row=1, column=1, padx=35)
        item_price_label = Label(scrollable_menu, text="Item Price", font=("Arial 10 bold"))
        item_price_label.grid(row=1, column=2, padx=35)
        item_qty_label = Label(scrollable_menu, text="Quantity Ordered", font=("Arial 10 bold"))
        item_qty_label.grid(row=1, column=3,padx=10)

        cursor.execute("SELECT * FROM menu_items")
        items = cursor.fetchall()
        row = 2
        global event_menu_items
        event_menu_items = []
        for item in items:
            label = Label(scrollable_menu, text=item[0], font=('Arial 9'))
            label.grid(row=row, column=0, sticky='n', pady=7)
            label = Label(scrollable_menu, text=item[1].strip(), font=('Arial 9'))
            label.grid(row=row, column=1, sticky='n', pady=7)
            label = Label(scrollable_menu, text=item[2], font=('Arial 9'))
            label.grid(row=row, column=2, sticky='n', pady=7)
            entry = Entry(scrollable_menu, font=('Arial 9'), width=5)
            entry.insert(0, 0)
            entry.grid(row=row, column=3, pady=7)
            row += 1
            event_menu_items.append([gl_event_id, item[0], item[2], entry])
        event_menu_items.insert(0, [customer, store, event_date])
        menucan.update_idletasks()
        menucan.yview_moveto(0)

def submit_event_clicked():
    running_total = 0
    cid = event_menu_items[0][0]
    store = event_menu_items[0][1]
    event_date = event_menu_items[0][2]
    eid = event_menu_items[1][0] 
    cursor = conn.cursor()
    for entry in event_menu_items[1:]:
        print(entry)
        quantity = int(entry[3].get())
        price = float(entry[2])
        if  quantity > 0:
            cursor.execute(f"INSERT INTO catering_event_items (event_id, menu_item_id, quantity) VALUES ({eid}, {entry[1]}, {quantity})")
            running_total += (quantity * price)
    cursor.execute(f"INSERT INTO invoices_to_customers (event_id, amt_due, due_date) VALUES ({eid}, {round(running_total,2)}, DATEADD(day,-2,(SELECT event_date FROM catering_events WHERE event_id={eid})))")
    cursor.execute(f"SELECT invoice_id FROM invoices_to_customers WHERE invoice_id=(SELECT max(invoice_id) FROM invoices_to_customers)")
    inv = cursor.fetchone()
    invid = inv[0]
    cursor.execute(f"INSERT INTO customer_payments (invoice_id) VALUES ({invid})")
    menu_items_data_frame.destroy()
    update_customers()
    change_catering_states()
    event_date_entry.delete(0, END)
    catering_buttons_container.lower()

def cancel_event_clicked():
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM catering_events WHERE event_id = {gl_event_id}")
    menu_items_data_frame.destroy()
    catering_buttons_cover.lift()
    change_catering_states()
    update_customers()
    event_date_entry.delete(0, END)

def start_order():
    bottom_buttons_container.lift()
    stoid = cb_new_order_store.get()
    supid = cb_new_order_sup.get()
    placed_date = date_placed_entry.get()
    received_date = date_received_entry.get()
    cursor = conn.cursor()
    if received_date == "":
        cursor.execute(f"INSERT INTO orders (supplier_id, store_id, order_placed_date) VALUES ({supid}, {stoid}, '{placed_date}')")
    else:
        cursor.execute(f"INSERT INTO orders (supplier_id, store_id, order_placed_date, order_received_date) VALUES ({supid}, {stoid}, '{placed_date}', '{received_date}')")
    cursor.execute("SELECT * FROM orders WHERE order_id=(SELECT max(order_id) FROM orders);")
    results = cursor.fetchall()
    global order_id
    for result in results:
        order_id = result[0]
    global supplier_items_frame
    supplier_items_frame = Frame(new_order_bottom_container, highlightbackground="black", highlightthickness=.5)
    itemcan = Canvas(supplier_items_frame, highlightthickness=0)
    itemcan.pack(side=LEFT, fill="both", expand="yes")
    items_vsb = Scrollbar(supplier_items_frame, orient=VERTICAL, command=itemcan.yview)
    items_vsb.pack(side=RIGHT, fill='y')
    itemcan.config(yscrollcommand=items_vsb.set)
    itemcan.bind('<Configure>', lambda e: itemcan.configure(scrollregion = itemcan.bbox('all')))
    scrollable_items = Frame(itemcan, highlightthickness=0)
    itemcan.create_window((0,0), window=scrollable_items)
    supplier_items_frame.place(relwidth=1, relheight=.9)

    header_label = Label(scrollable_items, text=f"Items available from supplier with ID: {supid}", font=("Helvetica 12 bold"))
    header_label.grid(row=0, column=0, columnspan=5)
    pn_label = Label(scrollable_items, text="Product Name", font=("Helvetica 10 bold"))
    pn_label.grid(row=1, column=0, sticky='w')
    pt_label = Label(scrollable_items, text="Product Type", font=("Helvetica 10 bold"))
    pt_label.grid(row=1, column=1, sticky='w')
    manu_label = Label(scrollable_items, text="Manufacturer", font=("Helvetica 10 bold"))
    manu_label.grid(row=1, column=2, sticky='w')
    ppc_label = Label(scrollable_items, text="Price", font=("Helvetica 10 bold"))
    ppc_label.grid(row=1, column=3, sticky='w')
    qty_label = Label(scrollable_items, text="Quantity Orderd", font=("Helvetica 10 bold"))
    qty_label.grid(row=1, column=4, sticky='w')

    stoid = cb_new_order_store.get()
    supid = cb_new_order_sup.get()
    cursor = conn.cursor()
    row = 2
    global order_entries
    order_entries = []
    
    cursor.execute(f"SELECT * FROM supplier_inventory WHERE supplier_id = {supid}")
    items = cursor.fetchall()
    for item in items:
        if item[0]:
            product_type = 'Bread'
            prodic = item[0]
        if item[1]:
            product_type = 'Coffee'
            prodic = item[1]
        if item[2]:
            product_type = 'Meat'
            prodic = item[2]
        if item[3]:
            product_type = 'Produce'
            prodic = item[3]
        if item[4]:
            product_type = 'Paper'
            prodic = item[4]
        if item[5]:
            product_type = 'Sugars, Spices, Seasonings'
            prodic = item[5]
        if item[6]:
            product_type = 'Other'
            prodic = item[6]
        if item[7]:
            product_type = 'Retail'
            prodic = item[7]
        if item[8]:
            product_type = 'Cleaning'
            prodic = item[8]
        if item[9]:
            product_type = 'Dairy'
            prodic = item[9]
        label = Label(scrollable_items, text=item[11], font=('Arial 9'))
        label.grid(row=row, column=0, sticky='w', pady=5)
        label = Label(scrollable_items, text=product_type, font=('Arial 9'))
        label.grid(row=row, column=1, sticky='w', pady=5)
        label = Label(scrollable_items, text=item[12], font=('Arial 9'))
        label.grid(row=row, column=2, sticky='w', pady=5)
        label = Label(scrollable_items, text=item[13], font=('Arial 9'))
        label.grid(row=row, column=3, sticky='w')
        entry = Entry(scrollable_items, font=('Arial 9'), width=5)
        entry.insert(0, 0)
        entry.grid(row=row, column=4, pady=5)
        row += 1
        order_entries.append([product_type, prodic, entry])
    itemcan.update_idletasks()
    itemcan.yview_moveto(0)

def cancel_order_clicked():
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM orders WHERE order_id = {order_id}")
    supplier_items_frame.destroy()
    bottom_buttons_container.lower()

def delete_event_view_orders():
    delete_event_tree.delete(*delete_event_tree.get_children())
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM events_with_names WHERE amt_paid = 0 AND COALESCE(canceled, 'false') != 'true'")
    results = cursor.fetchall()
    for result in results:
        fn = result[1].strip()
        ln = result[2].strip()
        n = fn + " " + ln
        delete_event_tree.insert("", index="end", values=(result[0], result[3], n, result[4], result[9], result[10]))

def del_event_tree_selected(event):
    delete_event_button['state'] = 'normal'
    mark_event_canceled_button['state'] = 'normal'

def delete_event_clicked():
    event_warning_message_del.lift()

def event_mark_cancel_cofirmed():
    selected_order = delete_event_tree.item(delete_event_tree.focus())
    order_details = selected_order['values']
    eid = order_details[0]
    cursor = conn.cursor()
    cursor.execute(f"UPDATE catering_events SET canceled = 1 WHERE event_id = {eid}")
    delete_event_tree.delete(*delete_event_tree.get_children())
    event_warning_message_cover.lift()

def event_mark_del_cofirmed():
    selected_order = delete_event_tree.item(delete_event_tree.focus())
    order_details = selected_order['values']
    eid = order_details[0]
    cursor = conn.cursor()
    cursor.execute(f"SELECT payment_id FROM events_with_names WHERE event_id = {eid}")
    pid = cursor.fetchone()[0]
    cursor.execute(f"DELETE FROM catering_events WHERE event_id = {eid}")
    cursor.execute(f"DELETE FROM invoices_to_customers WHERE event_id = {eid}")
    cursor.execute(f"DELETE FROM catering_event_items WHERE event_id = {eid}")
    cursor.execute(f"DELETE FROM customer_payments WHERE payment_id = {pid}")
    delete_event_tree.delete(*delete_event_tree.get_children())
    event_warning_message_cover.lift()

def submit_order_clicked():
    cursor = conn.cursor()
    for order in order_entries:
        qty = int(order[2].get())
        itemid = int(order[1])
        if order[0] == 'Dairy' and qty > 0:
            cursor.execute(f"INSERT INTO order_details (order_id, sup_dai_product_id, case_qty) VALUES ({order_id}, {itemid}, {qty})")
        if order[0] == 'Cleaning' and qty > 0:
            cursor.execute(f"INSERT INTO order_details (order_id, sup_cle_product_id, case_qty) VALUES ({order_id}, {itemid}, {qty})")
        if order[0] == 'Retail' and qty > 0:
            cursor.execute(f"INSERT INTO order_details (order_id, sup_ret_product_id, case_qty) VALUES ({order_id}, {itemid}, {qty})")
        if order[0] == 'Other' and qty > 0:
            cursor.execute(f"INSERT INTO order_details (order_id, sup_oth_product_id, case_qty) VALUES ({order_id}, {itemid}, {qty})")
        if order[0] == 'Sugars, Spices, Seasonings' and qty > 0:
            cursor.execute(f"INSERT INTO order_details (order_id, sup_sss_product_id, case_qty) VALUES ({order_id}, {itemid}, {qty})")
        if order[0] == 'Paper' and qty > 0:
            cursor.execute(f"INSERT INTO order_details (order_id, sup_pap_product_id, case_qty) VALUES ({order_id}, {itemid}, {qty})")
        if order[0] == 'Produce' and qty > 0:
            cursor.execute(f"INSERT INTO order_details (order_id, sup_pro_product_id, case_qty) VALUES ({order_id}, {itemid}, {qty})")
        if order[0] == 'Meat' and qty > 0:
            cursor.execute(f"INSERT INTO order_details (order_id, sup_mea_product_id, case_qty) VALUES ({order_id}, {itemid}, {qty})")
        if order[0] == 'Coffee' and qty > 0:
            cursor.execute(f"INSERT INTO order_details (order_id, sup_cof_product_id, case_qty) VALUES ({order_id}, {itemid}, {qty})")
        if order[0] == 'Bread' and qty > 0:
            cursor.execute(f"INSERT INTO order_details (order_id, sup_bre_product_id, case_qty) VALUES ({order_id}, {itemid}, {qty})")
    cursor.execute(f"SELECT * FROM order_report WHERE order_id = {order_id}")
    running_total = 0
    results = cursor.fetchall()
    due_date = payment_due_date_entry.get()
    for  result in results:
        running_total += (result[2] * result[3])
    cursor.execute(f"INSERT INTO supplier_invoices (order_id, amt_due, due_date) VALUES ({order_id}, {round(running_total, 2)}, '{due_date}')")
    cursor.execute(f"SELECT invoice_id FROM supplier_invoices WHERE invoice_id=(SELECT max(invoice_id) FROM supplier_invoices)")
    inv = cursor.fetchone()
    inv_id = inv[0]
    cursor.execute(f"INSERT INTO payments_to_suppliers (invoice_id) VALUES ({inv_id})")
    supplier_items_frame.destroy()
    cb_store.set("")
    cb_sup.set("")
    date_placed_entry.delete(0, END)
    payment_due_date_entry.insert(0, "")
    date_received_entry.insert(0, "")
    payment_due_date_entry.insert(0, "")
    bottom_buttons_cover.lift()

def get_cust_invoices_clicked():
    cust_log_pmt_frame_cover.lift()
    cust_invoices_tree.delete(*cust_invoices_tree.get_children())
    stoid = cust_inv_stores_cb.get()
    paid = cust_inv_var.get()
    cursor=conn.cursor()
    if paid == 'both':
        if stoid == 'All Stores':
            cursor.execute("SELECT * FROM events_with_names")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[5] != True:
                    cust_invoices_tree.insert("", index="end", values=(invoice[0], invoice[3], invoice[6], invoice[4], invoice[9], invoice[10]))
        else:
            cursor.execute(f"SELECT * FROM events_with_names WHERE store_id = {stoid}")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[5] != True:
                    cust_invoices_tree.insert("", index="end", values=(invoice[0], invoice[3], invoice[6], invoice[4], invoice[9], invoice[10]))
    if paid == 'paid':
        if stoid == 'All Stores':
            cursor.execute("SELECT * FROM events_with_names WHERE amt_due = amt_paid")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[5] != True:
                    cust_invoices_tree.insert("", index="end", values=(invoice[0], invoice[3], invoice[6], invoice[4], invoice[9], invoice[10]))
        else:
            cursor.execute(f"SELECT * FROM events_with_names WHERE store_id = {stoid} AND amt_due = amt_paid")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[5] != True:
                    cust_invoices_tree.insert("", index="end", values=(invoice[0], invoice[3], invoice[6], invoice[4], invoice[9], invoice[10]))

    else:
        if stoid == 'All Stores':
            cursor.execute("SELECT * FROM events_with_names WHERE amt_due > amt_paid")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[5] != True:
                    cust_invoices_tree.insert("", index="end", values=(invoice[0], invoice[3], invoice[6], invoice[4], invoice[9], invoice[10]))
        else:
            cursor.execute(f"SELECT * FROM events_with_names WHERE store_id = {stoid} AND amt_due > amt_paid")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[5] != True:
                    cust_invoices_tree.insert("", index="end", values=(invoice[0], invoice[3], invoice[6], invoice[4], invoice[9], invoice[10]))

def get_invoices_clicked():
    log_pmt_frame_cover.lift()
    invoices_tree.delete(*invoices_tree.get_children())
    stoid = inv_stores_cb.get()
    supid = inv_sups_cb.get()
    paid = inv_var.get()
    cursor=conn.cursor()
    if paid == 'both':
        if stoid == 'All Stores' and supid == 'All Suppliers':
            cursor.execute("SELECT * FROM order_payment_verification")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[8] != True:
                    invoices_tree.insert("", index="end", values=(invoice[0], invoice[5], invoice[3], invoice[1], invoice[6], invoice[7]))
        elif stoid == 'All Stores':
            cursor.execute(f"SELECT * FROM order_payment_verification WHERE supplier_id = {supid}")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[8] != True:
                    invoices_tree.insert("", index="end", values=(invoice[0], invoice[5], invoice[3], invoice[1], invoice[6], invoice[7]))
        elif supid == 'All Suppliers':
            cursor.execute(f"SELECT * FROM order_payment_verification WHERE store_id = {stoid}")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[8] != True:
                    invoices_tree.insert("", index="end", values=(invoice[0], invoice[5], invoice[3], invoice[1], invoice[6], invoice[7]))
        else:
            cursor.execute(f"SELECT * FROM order_payment_verification WHERE store_id = {stoid} AND supplier_id = {supid}")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[8] != True:
                    invoices_tree.insert("", index="end", values=(invoice[0], invoice[5], invoice[3], invoice[1], invoice[6], invoice[7]))
        
    if paid == 'paid':
        if stoid == 'All Stores' and supid == 'All Suppliers':
            cursor.execute("SELECT * FROM order_payment_verification WHERE amt_due = amt_paid")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[8] != True:
                    invoices_tree.insert("", index="end", values=(invoice[0], invoice[5], invoice[3], invoice[1], invoice[6], invoice[7]))
        elif stoid == 'All Stores':
            cursor.execute(f"SELECT * FROM order_payment_verification WHERE supplier_id = {supid} AND amt_due = amt_paid")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[8] != True:
                    invoices_tree.insert("", index="end", values=(invoice[0], invoice[5], invoice[3], invoice[1], invoice[6], invoice[7]))
        elif supid == 'All Suppliers':
            cursor.execute(f"SELECT * FROM order_payment_verification WHERE store_id = {stoid} AND amt_due = amt_paid")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[8] != True:
                    invoices_tree.insert("", index="end", values=(invoice[0], invoice[5], invoice[3], invoice[1], invoice[6], invoice[7]))
        else:
            cursor.execute(f"SELECT * FROM order_payment_verification WHERE store_id = {stoid} AND supplier_id = {supid} AND amt_due = amt_paid")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[8] != True:
                    invoices_tree.insert("", index="end", values=(invoice[0], invoice[5], invoice[3], invoice[1], invoice[6], invoice[7]))

    if paid == 'outstanding':
        if stoid == 'All Stores' and supid == 'All Suppliers':
            cursor.execute("SELECT * FROM order_payment_verification WHERE amt_paid < amt_due")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[8] != True:
                    invoices_tree.insert("", index="end", values=(invoice[0], invoice[5], invoice[3], invoice[1], invoice[6], invoice[7]))
        elif stoid == 'All Stores':
            cursor.execute(f"SELECT * FROM order_payment_verification WHERE amt_paid < amt_due AND supplier_id = {supid}")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[8] != True:
                    invoices_tree.insert("", index="end", values=(invoice[0], invoice[5], invoice[3], invoice[1], invoice[6], invoice[7]))
        elif supid == 'All Suppliers':
            cursor.execute(f"SELECT * FROM order_payment_verification WHERE amt_paid < amt_due AND supplier_id = {stoid}")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[8] != True:
                    invoices_tree.insert("", index="end", values=(invoice[0], invoice[5], invoice[3], invoice[1], invoice[6], invoice[7]))
        else:
            cursor.execute(f"SELECT * FROM order_payment_verification WHERE store_id = {stoid} AND supplier_id = {supid} AND amt_paid < amt_due")
            invoices = cursor.fetchall()
            for invoice in invoices:
                if invoice[8] != True:
                    invoices_tree.insert("", index="end", values=(invoice[0], invoice[5], invoice[3], invoice[1], invoice[6], invoice[7]))

def cust_invoice_selected(event):
    if cust_invoices_tree.focus():
        cust_inv_details_button['state'] = 'normal'
        cust_inv_pmt_button['state'] = 'normal'
    else:
        cust_inv_details_button['state'] = 'disabled'
        cust_inv_pmt_button['state'] = 'disabled'

def invoice_selected(event):
    if invoices_tree.focus():
        inv_details_button['state'] = 'normal'
        inv_pmt_button['state'] = 'normal'
        print("item selected")
    else:
        inv_details_button['state'] = 'disabled'
        inv_pmt_button['state'] = 'disabled'
        print("item deselected")

def cust_inv_details_clicked():
    if cust_invoices_tree.focus():
        cust_inv_details_frame.lift()
        selection = cust_invoices_tree.item(cust_invoices_tree.focus())
        selected_invoice = selection['values']
        eventid = selected_invoice[0]
        storeid = selected_invoice[1]
        cname = selected_invoice[3]
        paid = float(selected_invoice[5])
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM events_with_names WHERE event_id = {eventid}")
        invoice_details = cursor.fetchone()
        fn = invoice_details[1].strip()
        ln = invoice_details[2].strip()
        n = fn + " " + ln
        cust_inv_name.set(n)
        cust_inv_phone.set(invoice_details[8])
        cust_inv_email.set(invoice_details[7])
        cust_inv_date.set(invoice_details[4])
        if paid > 0:
            cust_payment_id.set(invoice_details[11])
            cust_pmt_amount.set(invoice_details[10])
            cust_pmt_date.set(invoice_details[12])
        else:
            cust_payment_id.set("N/A")
            cust_pmt_amount.set("N/A")
            cust_pmt_date.set("N/A")

def inv_details_clicked():
    if invoices_tree.focus():
        inv_details_frame.lift()
        selection = invoices_tree.item(invoices_tree.focus())
        selected_invoice = selection['values']
        orderid = selected_invoice[0]
        storeid = selected_invoice[1]
        supid = selected_invoice[2]
        paid = float(selected_invoice[5])
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM order_payment_verification WHERE order_id = {orderid}")
        invoice_details = cursor.fetchone()
        inv_supname.set(invoice_details[4])
        inv_date_placed.set(invoice_details[1])
        inv_date_rec.set(invoice_details[2])
        cursor.execute(f"select case_qty from order_details WHERE order_id = {orderid}")
        total_items = 0
        items = cursor.fetchall()
        for item in items:
            total_items += item[0]
        inv_items.set(total_items)
        cursor.execute(f"SELECT * FROM order_payment_verification WHERE order_id = {orderid}")
        if paid > 0:
            payment_details = cursor.fetchone()
            payment_id.set(payment_details[10])
            pmt_amount.set(payment_details[7])
            pmt_date.set(payment_details[11])
        else:
            payment_id.set("N/A")
            pmt_amount.set("N/A")
            pmt_date.set("N/A")

def cust_inv_payment_clicked():
    if cust_invoices_tree.focus():
        cust_log_pmt_frame.lift()
        selection = cust_invoices_tree.item(cust_invoices_tree.focus())
        selected_invoice = selection['values']
        amtdue = float(selected_invoice[4])
        amtpaid = float(selected_invoice[5])
        eid = selected_invoice[0]
        cursor = conn.cursor()
        if amtdue == amtpaid:
            cust_log_pmt_paid.lift()
        else:
            cust_log_pmt_details.lift()

def inv_payment_clicked():
    if invoices_tree.focus():
        log_pmt_frame.lift()
        selection = invoices_tree.item(invoices_tree.focus())
        selected_invoice = selection['values']
        amtdue = float(selected_invoice[4])
        amtpaid = float(selected_invoice[5])
        oid = selected_invoice[0]
        cursor = conn.cursor()
        if amtdue == amtpaid:
            log_pmt_paid.lift()
        else:
            log_pmt_details.lift()

def cust_submit_pmt_clicked():
    cursor = conn.cursor()
    date_paid = cust_date_paid_entry.get()
    selection = cust_invoices_tree.item(cust_invoices_tree.focus())
    selected_invoice = selection['values']
    eid = selected_invoice[0]
    cursor.execute(f"SELECT invoice_id FROM invoices_to_customers WHERE event_id={eid}")
    inv = cursor.fetchone()
    inv_id = inv[0]
    amtdue = float(selected_invoice[4])
    cursor.execute(f"UPDATE customer_payments SET amt_paid = {amtdue}, payment_date = '{date_paid}' WHERE invoice_id = {inv_id}")
    cust_log_pmt_frame.lower()
    cust_log_pmt_frame_cover.lift()
    cust_invoices_tree.delete(*cust_invoices_tree.get_children())

def submit_pmt_clicked():
    cursor = conn.cursor()
    date_paid = date_paid_entry.get()
    selection = invoices_tree.item(invoices_tree.focus())
    selected_invoice = selection['values']
    oid = selected_invoice[0]
    cursor.execute(f"SELECT invoice_id FROM supplier_invoices WHERE order_id={oid}")
    inv = cursor.fetchone()
    inv_id = inv[0]
    amtdue = float(selected_invoice[4])
    cursor.execute(f"UPDATE payments_to_suppliers SET amt_paid = {amtdue}, payment_date = '{date_paid}' WHERE invoice_id = {inv_id}")
    log_pmt_frame.lower()
    log_pmt_frame_cover.lift()
    invoices_tree.delete(*invoices_tree.get_children())

def submit_date_changes():
    selected_order = orders_tree.item(orders_tree.focus())
    order_details = selected_order['values']
    oid = order_details[0]
    date_placed = edit_place_date_entry.get()
    date_rec = edit_rec_date_entry.get()
    cursor = conn.cursor()
    if date_rec == 'None':
        cursor.execute(f"UPDATE orders SET order_placed_date = '{date_placed}' WHERE order_id = {oid}")
    else:
        cursor.execute(f"UPDATE orders SET order_placed_date = '{date_placed}', received_date = '{date_rec}' WHERE order_id = {oid}")
    orders_tree.delete(*orders_tree.get_children())
    orders_details_tree.delete(*orders_details_tree.get_children())
    edit_rec_submit_button['state'] = 'disabled'
    edit_rec_date_entry.delete(0, END)
    edit_place_date_entry.delete(0, END)

def delete_order_view_orders():
    delete_order_tree.delete(*delete_order_tree.get_children())
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM order_payment_verification WHERE amt_paid = 0 AND received_date IS NULL AND COALESCE(canceled, 'false') != 'true'")
    results = cursor.fetchall()
    for result in results:
        delete_order_tree.insert("", index="end", values=(result[0], result[5], result[1], result[2], result[6], result[7]))

def mark_as_canceled_clicked():
    warning_message_cancel.lift()

def mark_event_as_canceled_clicked():
    event_warning_message_cancel.lift()

def delete_order_clicked():
    warning_message_del.lift()

def mark_cancel_cofirmed():
    selected_order = delete_order_tree.item(delete_order_tree.focus())
    order_details = selected_order['values']
    oid = order_details[0]
    cursor = conn.cursor()
    cursor.execute(f"UPDATE orders SET canceled = 1 WHERE order_id = {oid}")
    delete_order_tree.delete(*delete_order_tree.get_children())
    warning_message_cover.lift()


def mark_del_cofirmed():
    selected_order = delete_order_tree.item(delete_order_tree.focus())
    order_details = selected_order['values']
    oid = order_details[0]
    cursor = conn.cursor()
    cursor.execute(f"SELECT payment_id FROM order_payment_verification WHERE order_id = {oid}")
    pid = cursor.fetchone()[0]
    cursor.execute(f"DELETE FROM orders WHERE order_id = {oid}")
    cursor.execute(f"DELETE FROM supplier_invoices WHERE order_id = {oid}")
    cursor.execute(f"DELETE FROM order_details WHERE order_id = {oid}")
    cursor.execute(f"DELETE FROM payments_to_suppliers WHERE payment_id = {pid}")
    delete_order_tree.delete(*delete_order_tree.get_children())
    warning_message_cover.lift()

def del_order_tree_selected(event):
    delete_order_button['state'] = 'normal'
    mark_as_canceled_button['state'] = 'normal'

def update_customers():
    customers_tree.delete(*customers_tree.get_children())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers ORDER BY first_name ASC")
    customers = cursor.fetchall()
    for customer in customers:
        customers_tree.insert("", index=END, values=(customer[0], customer[1], customer[2], customer[3], customer[4]))
    try:
        update_customer_list()
    except NameError:
        print("first run catch")

def update_customer_list():
    customer_list_tree.delete(*customer_list_tree.get_children())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers ORDER BY first_name ASC")
    customers = cursor.fetchall()
    for customer in customers:
        fname = customer[1].strip()
        l_initial = customer[2][0].strip() + "."
        name = fname + ", " + l_initial
        customer_list_tree.insert("", index=END, values=(customer[0], name))

def update_menu():
    menu_tree.delete(*menu_tree.get_children())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu_items")
    items = cursor.fetchall()
    for item in items:
        menu_tree.insert("", index=END, values=(item[0], item[1], item[2]))

def add_new_customer_clicked():
    new_customer_entry_container.lift()
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)

def add_new_menu_clicked():
    new_menu_entry_container.lift()
    item_name_entry.delete(0, END)
    item_price_entry.delete(0, END)

def confirm_new_customer_clicked():
    cursor = conn.cursor()
    fn = first_name_entry.get()
    ln = last_name_entry.get()
    ph = phone_entry.get()
    em = email_entry.get()
    cursor.execute(f"INSERT INTO customers (first_name, last_name, phone, email) VALUES ('{fn}', '{ln}', '{ph}', '{em}')")
    update_customers()
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    customer_data_cover.lift()

def confirm_new_menu_clicked():
    cursor = conn.cursor()
    name = item_name_entry.get()
    price = item_price_entry.get()
    cursor.execute(f"INSERT INTO menu_items (item_name, price) VALUES ('{name}', {price})")
    update_menu()
    item_name_entry.delete(0, END)
    item_price_entry.delete(0, END)
    menu_data_cover.lift()

def edit_customer_clicked():
    if customers_tree.focus():
        edit_customer_container.lift()
        selected_customer = customers_tree.item(customers_tree.focus())
        customer = selected_customer['values']
        cid = customer[0]
        efirst_name_entry.delete(0, END)
        elast_name_entry.delete(0, END)
        ephone_entry.delete(0, END)
        eemail_entry.delete(0, END)
        efirst_name_entry.insert(0, customer[1])
        elast_name_entry.insert(0, customer[2])
        ephone_entry.insert(0, customer[3])
        eemail_entry.insert(0, customer[4])
        e_cid.set(cid)

def edit_menu_clicked():
    if menu_tree.focus():
        edit_menu_container.lift()
        selected_item = menu_tree.item(menu_tree.focus())
        item = selected_item['values']
        mid = item[0]
        eitem_name_entry.delete(0, END)
        eitem_price_entry.delete(0, END)
        eitem_name_entry.insert(0, item[1])
        eitem_price_entry.insert(0, item[2])
        e_mid.set(mid)

def confirm_edit_customer_clicked():
    cursor = conn.cursor()
    fn = efirst_name_entry.get()
    ln = elast_name_entry.get()
    pn = ephone_entry.get()
    em = eemail_entry.get()
    c_id = ecid_label2.cget('text')
    cursor.execute(f"UPDATE customers SET first_name = '{fn}', last_name = '{ln}', phone = '{pn}', email = '{em}' WHERE customer_id = '{c_id}'")
    customer_data_cover.lift()
    update_customers()
    efirst_name_entry.delete(0, END)
    elast_name_entry.delete(0, END)
    ephone_entry.delete(0, END)
    eemail_entry.delete(0, END)

def confirm_edit_menu_clicked():
    cursor = conn.cursor()
    name = eitem_name_entry.get()
    price = eitem_price_entry.get()
    m_id = emid_label2.cget('text')
    cursor.execute(f"UPDATE menu_items SET item_name = '{name}', price = {price} WHERE menu_item_id = {m_id}")
    menu_data_cover.lift()
    update_menu()
    eitem_price_entry.delete(0, END)
    eitem_name_entry.delete(0, END)

def manage_customers_clicked():
    manage_customers_main_frame.lift()

def manage_menu_clicked():
    manage_menu_main_frame.lift()

def del_customer_clicked():
    if customers_tree.focus():
        delete_customer_container.lift()
        selected_customer = customers_tree.item(customers_tree.focus())
        customer = selected_customer['values']
        global cid
        cid = customer[0]
        cursor = conn.cursor()
        cursor.execute(f"SELECT customer_id FROM catering_events WHERE customer_id = {cid}")
        results = cursor.fetchone()
        if results:
            del_customer_error.lift()
        else:
            del_customer_label_container.lift()

def del_menu_clicked():
    if menu_tree.focus():
        delete_menu_container.lift()
        selected_item = menu_tree.item(menu_tree.focus())
        item = selected_item['values']
        global mid
        mid = item[0]
        cursor = conn.cursor()
        cursor.execute(f"SELECT menu_item_id FROM catering_event_report WHERE menu_item_id = {mid}")
        results = cursor.fetchone()
        if results:
            del_menu_error.lift()
        else:
            del_menu_label_container.lift()

def delete_customer_confirmed():
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM customers WHERE customer_id = {cid}")
    update_customers()
    customer_data_cover.lift()

def delete_menu_confirmed():
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM menu_items WHERE menu_item_id = {mid}")
    update_menu()
    menu_data_cover.lift()

def create_event_clicked():
    create_event_main_frame.lift()
    update_customer_list()

def view_events_clicked():
    events_tree.delete(*events_tree.get_children())
    view_events_main_frame.lift()

def cancel_catering_event_clicked():
    delete_event_main_frame.lift()

def add_user():
    add_user_frame.lift()

def edit_user():
    if users_tree.focus():
        edit_user_frame.lift()
        user_info = users_tree.item(users_tree.focus())
        global uid
        uid = user_info['values'][0]
        un = user_info['values'][1]
        usr.set(f"Please enter a new password for user: {un}")

def new_pw_confirm():
    cursor = conn.cursor()
    newpw = new_pw_entry.get()
    cursor.execute(f"UPDATE system_users SET password = '{newpw}' WHERE user_id = {uid}")
    edit_user_frame.lower()

def confirm_del_user():
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM system_users WHERE user_id = {del_uid}") 
    del_user_frame.lower()
    update_users()

def delete_user():
    if users_tree.focus():
        del_user_frame.lift()
        user_info = users_tree.item(users_tree.focus())
        global del_uid
        del_uid = user_info['values'][0]
        un = user_info['values'][1].strip()
        d_usr.set(f"Are you sure you want to delete the user: {un}?\nThis action CANNOT be undone.")
        

def confirm_new_user():
    un = un_entry.get()
    pw = password_entry.get()
    if admin_cb.get() == 'Yes':
        adm = 1
    else: 
        adm = 0
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO system_users (username, password, admin) VALUES ('{un}', '{pw}', {adm})")
    add_user_frame.lower()
    un_entry.delete(0, END)
    password_entry.delete(0, END)
    update_users()

def get_items_to_order_report():
    items_to_order_tree.delete(*items_to_order_tree.get_children())
    prod = items_to_order_prod_cb.get()
    stoid = items_to_order_store_cb.get()
    cursor = conn.cursor()
    if prod == 'Bread':
        cursor.execute(f"SELECT * FROM bread_qty_to_order WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[3]) - int(result[2]))
            items_to_order_tree.insert("", END, values=(result[0], result[8], result[4], result[2], result[3], amt))
    if prod == 'Cleaning':
        cursor.execute(f"SELECT * FROM cleaning_qty_to_order WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[3]) - int(result[2]))
            items_to_order_tree.insert("", END, values=(result[0], result[8], result[4], result[2], result[3], amt))
    if prod == 'Coffee':
        cursor.execute(f"SELECT * FROM coffee_qty_to_order WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[3]) - int(result[2]))
            items_to_order_tree.insert("", END, values=(result[0], result[8], result[4], result[2], result[3], amt))
    if prod == 'Dairy':
        cursor.execute(f"SELECT * FROM dairy_qty_to_order WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[3]) - int(result[2]))
            items_to_order_tree.insert("", END, values=(result[0], result[8], result[4], result[2], result[3], amt))
    if prod == 'Meat':
        cursor.execute(f"SELECT * FROM meat_qty_to_order WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[3]) - int(result[2]))
            items_to_order_tree.insert("", END, values=(result[0], result[8], result[4], result[2], result[3], amt))
    if prod == 'Paper':
        cursor.execute(f"SELECT * FROM paper_qty_to_order WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[3]) - int(result[2]))
            items_to_order_tree.insert("", END, values=(result[0], result[8], result[4], result[2], result[3], amt))
    if prod == 'Produce':
        cursor.execute(f"SELECT * FROM produce_qty_to_order WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[3]) - int(result[2]))
            items_to_order_tree.insert("", END, values=(result[0], result[8], result[4], result[2], result[3], amt))
    if prod == 'Retail':
        cursor.execute(f"SELECT * FROM retail_qty_to_order WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[3]) - int(result[2]))
            items_to_order_tree.insert("", END, values=(result[0], result[8], result[4], result[2], result[3], amt))
    if prod == 'Sugars, Spices, Seasonings':
        cursor.execute(f"SELECT * FROM sss_qty_to_order WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[3]) - int(result[2]))
            items_to_order_tree.insert("", END, values=(result[0], result[8], result[4], result[2], result[3], amt))

def get_inc_items_report():
    inc_items_tree.delete(*inc_items_tree.get_children())
    prod = inc_items_prod_cb.get()
    stoid = inc_items_store_cb.get()
    cursor = conn.cursor()
    if prod == 'Bread':
        cursor.execute(f"SELECT * FROM incorrectly_ordered_bread_products WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[5]) - int(result[4]))
            inc_items_tree.insert("", END, values=(result[0], result[1], result[2], result[4], result[3], amt))
    if prod == 'Cleaning':
        cursor.execute(f"SELECT * FROM incorrectly_ordered_cleaning_products WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[5]) - int(result[4]))
            inc_items_tree.insert("", END, values=(result[0], result[1], result[2], result[4], result[3], amt))
    if prod == 'Coffee':
        cursor.execute(f"SELECT * FROM incorrectly_ordered_coffee_products WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[5]) - int(result[4]))
            inc_items_tree.insert("", END, values=(result[0], result[1], result[2], result[4], result[3], amt))
    if prod == 'Dairy':
        cursor.execute(f"SELECT * FROM incorrectly_ordered_dairy_products WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[5]) - int(result[4]))
            inc_items_tree.insert("", END, values=(result[0], result[1], result[2], result[4], result[3], amt))
    if prod == 'Meat':
        cursor.execute(f"SELECT * FROM incorrectly_ordered_meat_products WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[5]) - int(result[4]))
            inc_items_tree.insert("", END, values=(result[0], result[1], result[2], result[4], result[3], amt))
    if prod == 'Paper':
        cursor.execute(f"SELECT * FROM incorrectly_ordered_paper_products WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[5]) - int(result[4]))
            inc_items_tree.insert("", END, values=(result[0], result[1], result[2], result[4], result[3], amt))
    if prod == 'Produce':
        cursor.execute(f"SELECT * FROM incorrectly_ordered_produce_products WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[5]) - int(result[4]))
            inc_items_tree.insert("", END, values=(result[0], result[1], result[2], result[4], result[3], amt))
    if prod == 'Retail':
        cursor.execute(f"SELECT * FROM incorrectly_ordered_retail_products WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[5]) - int(result[4]))
            inc_items_tree.insert("", END, values=(result[0], result[1], result[2], result[4], result[3], amt))
    if prod == 'Sugars, Spices, Seasonings':
        cursor.execute(f"SELECT * FROM incorrectly_ordered_sss_products WHERE store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            amt = (int(result[5]) - int(result[4]))
            inc_items_tree.insert("", END, values=(result[0], result[1], result[2], result[4], result[3], amt))

def view_canceled_orders():
    canceled_orders_tree.delete(*canceled_orders_tree.get_children())
    stoid = canceled_orders_store_cb.get()
    cursor = conn.cursor()
    it_cursor = conn.cursor()
    if stoid == 'All Stores':
        cursor.execute("SELECT * FROM order_payment_verification WHERE canceled = 1")
        results = cursor.fetchall()
        for result in results:
            o_id = result[0]
            total_items = 0
            it_cursor.execute(f"select case_qty from order_details WHERE order_id = {o_id}")
            itms = it_cursor.fetchall()
            for itm in itms:
                total_items += itm[0]
            canceled_orders_tree.insert("", END, values=(result[5], result[0], result[4], result[1], total_items, result[6]))
    else:
        cursor.execute(f"SELECT * FROM order_payment_verification WHERE canceled = 1 AND store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            o_id = result[0]
            total_items = 0
            it_cursor.execute(f"select case_qty from order_details WHERE order_id = {o_id}")
            itms = it_cursor.fetchall()
            for itm in itms:
                total_items += itm[0]
            canceled_orders_tree.insert("", END, values=(result[5], result[0], result[4], result[1], total_items, result[6]))

def view_canceled_events():
    canceled_events_tree.delete(*canceled_events_tree.get_children())
    stoid = canceled_events_store_cb.get()
    cursor = conn.cursor()
    if stoid == 'All Stores':
        cursor.execute("SELECT * FROM events_with_names WHERE canceled = 1")
        results = cursor.fetchall()
        for result in results:
            n = result[1].strip() + " " + result[2].strip()
            canceled_events_tree.insert("", END, values=(result[3], result[0], n, result[4], result[9]))
    else:
        cursor.execute(f"SELECT * FROM events_with_names WHERE canceled = 1 AND store_id = {stoid}")
        results = cursor.fetchall()
        for result in results:
            n = result[1].strip() + " " + result[2].strip()
            canceled_events_tree.insert("", END, values=(result[3], result[0], result[4], n, result[9]))

def canceled_event_reports():
    canceled_event_frame.lift()

def canceled_orders_reports():
    canceled_orders_frame.lift()

def items_to_order_reports():
    items_to_order_frame.lift()

def items_incorrectly_ordered_reports():
    inc_items_frame.lift()


#Saving store list
all_stores = []
stores_with_all = ['All Stores']
all_customers = []
customers_with_all = ['All Customers']
sups = []
all_sups = ['All Suppliers']

#DB Connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=CoT-CIS3365-12.cougarnet.uh.edu,1433;DATABASE=Blockhouse_DB;UID=cis3365;PWD=cis3365')


root = Tk()
root.title("Blockhouse Management System")

#Using canvas to set initial window size
canvas = Canvas(root, bg='white', height=HEIGHT, width=WIDTH)

#This label sets the background image
bg_img = PhotoImage(file="coffee.png")
bg_label = Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas.pack()

#The container that holds the log in screen
login_container = Frame(root, bg='#454040', bd=25, highlightbackground="#332e2d", highlightthickness=2)
login_container.place(relx=.5, rely=.5, anchor='c')
title_label = Label(login_container, text="Welcome to the Blockhouse Inventory System!", bg='#454040', fg='white', font=('Helvetica 12 bold'))
title_label.grid(row=0, column=0, columnspan=2, pady=15)
username_label = Label(login_container, text="Username", bg='#454040', fg='white')
username_label.grid(row=1, column=0, padx=10, pady=15)
username_entry = Entry(login_container)
username_entry.grid(row=1, column=1, pady=15)
pw_label = Label(login_container, text="Password", bg='#454040', fg='white')
pw_label.grid(row=2, column=0)
pw_entry = Entry(login_container, show="*")
pw_entry.grid(row=2, column=1)
login_button = Button(login_container, text="Log In", command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=25)

#This frame is brought to the front after a successful admin login
admin_logged_in = Frame(root, bg='#454040', highlightbackground="#332e2d", highlightthickness=1)
admin_logged_in.place(relx=.5, rely=.5, anchor='c', width=968, height=738)

#This code styles the font on the notebook tabs
s = ttk.Style()
s.configure('TNotebook.Tab', padding=5, bg='black', fg='grey', font=('Helvetica 12') )

##BEGIN ADMIN NOTEBOOK##
#Using a notebook for simplified navigation
admin_notebook = ttk.Notebook(admin_logged_in)
admin_notebook.pack(fill="both", expand=True)

#Creating a frame for each tab of the notebook
admin_main_frame = Frame(admin_notebook, width=968, height=738)
admin_store_frame = Frame(admin_notebook, width=968, height=738)
admin_system_users_frame = Frame(admin_notebook, width=968, height=738)
admin_inventory_frame = Frame(admin_notebook, width=968, height=738)
admin_orders_frame = Frame(admin_notebook, width=968, height=738)
admin_catering_frame = Frame(admin_notebook, width=968, height=738)
admin_reports_frame = Frame(admin_notebook, width=968, height=738)
admin_main_frame.pack(fill="both", expand=1)
admin_store_frame.pack(fill="both", expand=1)
admin_system_users_frame.pack(fill="both", expand=1)
admin_inventory_frame.pack(fill="both", expand=1)
admin_orders_frame.pack(fill="both", expand=1)
admin_catering_frame.pack(fill="both", expand=1)
admin_reports_frame.pack(fill="both", expand=1)

#BEGIN WELCOME TAB
admin_notebook.add(admin_main_frame, text="Welcome Page")
un_admin_text = StringVar()
welcome_un = Label(admin_main_frame, textvariable=un_admin_text, font=('Arial 14'))
welcome_un.pack(anchor="center", pady=20)
welcome_label = Label(admin_main_frame, font=('Arial 14'), text=f"You are logged in to the Blockhouse Inventory Management System with admin privileges.\n Use the tabs above to see all available options.")
welcome_label.pack(anchor="center", pady=25)
logout_button = Button(admin_main_frame, text="Logout", command=logout_clicked, font=('Arial 10'))
logout_button.pack(anchor="center")
#END WELCOME TAB

#BEGIN STORES TAB
admin_notebook.add(admin_store_frame, text="Stores")

store_tree_container = Frame(admin_store_frame)
store_tree_container.place(relwidth=1, relheight=.6)
store_tree = ttk.Treeview(store_tree_container)
store_tree['show'] = 'headings'
store_tree['columns'] = ("Store ID", "State ID", "City", "Address")
store_tree.column("#0", width=0, anchor=W)
store_tree.column("Store ID", anchor=W, width=20)
store_tree.column("State ID", anchor=W, width=20)
store_tree.column("City", anchor=W, width=50)
store_tree.column("Address", anchor=W, width=200)

store_tree.heading("#0")
store_tree.heading("Store ID", text="Store ID", anchor=W)
store_tree.heading("State ID", text="State ID", anchor=W)
store_tree.heading("City", text="City", anchor=W)
store_tree.heading("Address", text="Address", anchor=W)

store_tree.pack(fill=BOTH, expand=YES)
update_stores()

store_button_container = Frame(admin_store_frame)
store_button_container.place(relwidth=1, relheight=.12, rely=.6)
store_buttons = Frame(store_button_container)
store_buttons.pack(anchor=N, pady=15)
add_store_button = Button(store_buttons, text="Add a new store", command=add_store, pady=10)
add_store_button.grid(column=0, row=0, padx=10)
edit_store_button = Button(store_buttons, text="Edit Selected Store", command=edit_store, pady=10)
edit_store_button.grid(column=1, row=0, padx=10)

entry_frame_container = Frame(admin_store_frame)
entry_frame_container.place(relwidth=1, relheight=.3, rely=.7)
entry_frame_cover = Frame(entry_frame_container)
entry_frame_cover.place(relwidth=1, relheight=1)
add_store_data = Frame(entry_frame_container)
add_store_data.place(relwidth=1, relheight=1)
add_store_frame = Frame(add_store_data)
add_store_frame.pack(anchor=N, pady=20)
state_id_label = Label(add_store_frame, text="State ID:", font=("Helvetica 12"))
state_id_label.grid(column=0, row=0, padx=15, sticky=E)
state_id_entry = Entry(add_store_frame, width=30, font=("Arial 12"))
state_id_entry.grid(column=1, row=0, padx=15)
city_label = Label(add_store_frame, text="City:", font=("Helvetica 12"))
city_label.grid(column=0, row=1, padx=15, sticky=E)
city_entry = Entry(add_store_frame, width=30, font=("Arial 12"))
city_entry.grid(column=1, row=1, padx=15)
address_label = Label(add_store_frame, text="Address:", font=("Helvetica 12"))
address_label.grid(column=0, row=2, padx=15, sticky=E)
address_entry = Entry(add_store_frame, width=30, font=("Arial 12"))
address_entry.grid(column=1, row=2, padx=15)
submit_button = Button(add_store_frame, text="Submit", command=submit_new_store)
submit_button.grid(row=3, column=0, pady=15)
cancel_button = Button(add_store_frame, text="Cancel", command=entry_frame_cover.lift)
cancel_button.grid(row=3, column=1,  pady=15)
add_store_data.lower()

edit_store_data = Frame(entry_frame_container)
edit_store_data.place(relwidth=1, relheight=1)
update_store_frame = Frame(edit_store_data)
update_store_frame.pack(anchor=N, pady=20)
store_id_text = StringVar()
store_id_label = Label(update_store_frame, text="Store ID:", font=("Helvetica 12"))
store_id_label.grid(column=0, row=0, padx=15)
store_id_label2 = Label(update_store_frame, textvariable=store_id_text, font=("Helvetica 12"))
store_id_label2.grid(column=1, row=0, padx=15)
state_id_label = Label(update_store_frame, text="State ID:", font=("Helvetica 12"))
state_id_label.grid(column=0, row=1, padx=15)
state_id_entry_update = Entry(update_store_frame, width=30, font=("Arial 12"))
state_id_entry_update.grid(column=1, row=1, padx=15)
city_label = Label(update_store_frame, text="City:", font=("Helvetica 12"))
city_label.grid(column=0, row=2, padx=15)
city_entry_update = Entry(update_store_frame, width=30, font=("Arial 12"))
city_entry_update.grid(column=1, row=2, padx=15)
address_label = Label(update_store_frame, text="Address:", font=("Helvetica 12"))
address_label.grid(column=0, row=3, padx=15)
address_entry_update = Entry(update_store_frame, width=30, font=("Arial 12"))
address_entry_update.grid(column=1, row=3, padx=15)
submit_button = Button(update_store_frame, text="Submit", command=update_store)
submit_button.grid(row=4, column=0,  pady=15)
cancel_button = Button(update_store_frame, text="Cancel", command=entry_frame_cover.lift)
cancel_button.grid(row=4, column=1,  pady=15)
edit_store_data.lower()
#END STORES TAB

#BEGIN SYSTEM USERS TAB
admin_notebook.add(admin_system_users_frame, text="System Users")

users_tree_container = Frame(admin_system_users_frame)
users_tree_container.place(relwidth=1, relheight=.6)
users_tree = ttk.Treeview(users_tree_container, selectmode='browse')
users_tree['show'] = 'headings'
users_tree['columns'] = ("User ID", "Username", "Admin")

users_tree.column("#0", width=0)
users_tree.column("User ID", anchor=W, width=20)
users_tree.column("Username", anchor=W, width=50)
users_tree.column("Admin", anchor=W, width=30)

users_tree.heading("#0")
users_tree.heading("User ID", text="User ID", anchor=W)
users_tree.heading("Username", text="Username", anchor=W)
users_tree.heading("Admin", text="Admin Privileges", anchor=W)

users_tree.pack(fill=BOTH, expand=YES)

users_vsb = ttk.Scrollbar(admin_system_users_frame, orient="vertical", command=users_tree.yview)
users_vsb.place(x=940, y=2, height=415)
users_tree.configure(yscrollcommand=users_vsb.set)

users_button_container = Frame(admin_system_users_frame)
users_button_container.place(relwidth=1, relheight=.12, rely=.6)
users_buttons = Frame(users_button_container)
users_buttons.pack(anchor=N, pady=10)
add_user_button = Button(users_buttons, text="Add a new user", command=add_user, pady=10, font=("Helvetica 10"))
add_user_button.grid(column=0, row=0, padx=10)
edit_user_button = Button(users_buttons, text="Reset selected user's password", command=edit_user, pady=10, font=("Helvetica 10"))
edit_user_button.grid(column=1, row=0, padx=10)
delete_user_button = Button(users_buttons, text="Delete selected user", command=delete_user, pady=10, font=("Helvetica 10"))
delete_user_button.grid(column=2, row=0, padx=10)

users_bottom_container = Frame(admin_system_users_frame)
users_bottom_container.place(relwidth=1, rely=.72, relheight=.28)
users_bottom_cover = Frame(users_bottom_container)
users_bottom_cover.place(relheight=1, relwidth=1)

add_user_frame = Frame(users_bottom_container)
add_user_frame.place(relheight=1, relwidth=1)
add_user_data = Frame(add_user_frame)
add_user_data.pack(anchor=N)
username_label = Label(add_user_data, text="Create username:")
username_label.grid(row=0, column=0, padx=10, pady=15)
un_entry = Entry(add_user_data)
un_entry.grid(row=0, column=1, padx=10, pady=15)
password_label = Label(add_user_data, text="Create password:")
password_label.grid(row=0, column=2, padx=10, pady=15)
password_entry = Entry(add_user_data, show="*")
password_entry.grid(row=0, column=3, padx=10, pady=15)
admin_cb_label = Label(add_user_data, text="Is this an admin account?")
admin_cb_label.grid(row=0, column=4, padx=10, pady=15)
admin_cb = ttk.Combobox(add_user_data, values=['Yes', 'No'], state='readonly')
admin_cb.grid(row=0, column=5)
confirm_new_user_button = Button(add_user_data, text="Create New User", command=confirm_new_user, width=20)
confirm_new_user_button.grid(row=1, column=1, columnspan=2)
cancel_new_user_button = Button(add_user_data, text="Cancel", command=add_user_frame.lower, width=20)
cancel_new_user_button.grid(row=1, column=3, columnspan=2)
add_user_frame.lower()

edit_user_frame = Frame(users_bottom_container)
edit_user_frame.place(relheight=1, relwidth=1)
edit_user_data = Frame(edit_user_frame)
edit_user_data.pack(anchor=N)
usr = StringVar()
new_pw_label = Label(edit_user_data, textvariable=usr, font="Helvetica 12 bold")
new_pw_label.pack(anchor=N, pady=15)
new_pw_entry = Entry(edit_user_data, width=30, show="*")
new_pw_entry.pack(anchor=N, pady=10)
new_pw_submit = Button(edit_user_data, text="Change Password", command=new_pw_confirm)
new_pw_submit.pack(anchor=N, pady=10)
new_pw_cancel = Button(edit_user_data, text="CANCEL", command=edit_user_frame.lower())
new_pw_cancel.pack(anchor=N, pady=10)
edit_user_frame.lower()


del_user_frame = Frame(users_bottom_container)
del_user_frame.place(relheight=1, relwidth=1)
del_user_data = Frame(del_user_frame)
del_user_data.pack(anchor=N)
d_usr = StringVar()
del_user_warning = Label(del_user_data, textvariable=d_usr, pady=20, font=("Helvetica 14 bold"))
del_user_warning.pack(anchor=N)
del_user_confirm = Button(del_user_data, text="CONFIRM", command=confirm_del_user)
del_user_confirm.pack(anchor=N, pady=10)
del_user_cancel = Button(del_user_data, text="Cancel", command=del_user_frame.lower)
del_user_cancel.pack(anchor=N)
del_user_frame.lower()

update_users()
#END SYSTEM USERS TAB

#BEGIN ADMIN INVENTORY TAB
admin_notebook.add(admin_inventory_frame, text="Inventory")
inventory_button_container = Frame(admin_inventory_frame, bg='grey')
inventory_button_container.pack(side="left", fill="y")
manage_products_button = Button(inventory_button_container, text="Manage Products", command=manage_products_clicked)
manage_products_button.pack(pady=10, fill=X)
manage_suppliers_button = Button(inventory_button_container, text="Manage Suppliers", command=manage_suppliers_clicked)
manage_suppliers_button.pack(pady=10, fill=X)
update_counts_button = Button(inventory_button_container, text="Update Counts", command=counts_clicked)
update_counts_button.pack(pady=10, fill=X)
inventory_data_container = Frame(admin_inventory_frame)
inventory_data_container.pack(fill='both', expand=True)


inventory_main_frame = Frame(inventory_data_container)
inventory_main_frame.place(relwidth=1, relheight=1)
main_frame_message = Label(inventory_main_frame, text="Please select an option from the left", font=('Helvetica 20 bold'))
main_frame_message.place(relx=.25, rely=.3)

#begin products
products_main_frame = Frame(inventory_data_container)
products_main_frame.place(relwidth=1, relheight=1)
products_frame = Frame(products_main_frame)
products_frame.place(relwidth=1, relheight=.5)
products_header = Label(products_frame, text="Select a product category below", font=('Helvetica 12 bold'))
products_header.pack()
options = ["Bread", "Cleaning", "Coffee", "Dairy", "Meat", "Other", "Paper", "Produce", "Retail", "Sugars, Spices, Seasonings"]
options_svar = StringVar()
options_svar.set("")
products_cb = ttk.Combobox(products_frame, textvariable=options_svar, values=options)
products_cb.pack(pady=5, fill='x', padx=30)
products_cb.bind("<<ComboboxSelected>>", cb_product_selected)

products_tree = ttk.Treeview(products_frame)
products_tree['show'] = 'headings'
products_tree['columns'] = ("Product ID", "Supplier ID", "Product Name", "Manufacturer", "Price per case", "Case Quantity")
products_tree.pack(fill='x')
products_main_frame.lower()

products_tree.column("Product ID", width=10, anchor='center')
products_tree.column("Supplier ID", width=10, anchor='center')
products_tree.column("Product Name", width=50)
products_tree.column("Manufacturer", width=50)
products_tree.column("Price per case", width=50, anchor='center')
products_tree.column("Case Quantity", width=50, anchor='w')

products_tree.heading("Product ID", text="Product ID")
products_tree.heading("Supplier ID", text="Supplier ID")
products_tree.heading("Product Name", text="Product Name")
products_tree.heading("Manufacturer", text="Manufacturer")
products_tree.heading("Price per case", text="Price per Case")
products_tree.heading("Case Quantity", text="Case Quantity")

products_vsb = ttk.Scrollbar(products_frame, orient="vertical", command=products_tree.yview)
products_vsb.place(x=835, y=60, height=222)
products_tree.configure(yscrollcommand=products_vsb.set)

bottom_container_cover = Frame(products_main_frame)
bottom_container_cover.place(relheight=.5, relwidth=1, rely=.4)
product_bottom_container = Frame(products_main_frame)
product_bottom_container.place(relheight=.5, relwidth=1, rely=.4)
product_buttons_container = Frame(product_bottom_container)
product_buttons_container.place(relheight=1, relwidth=.2)
add_product_button = Button(product_buttons_container, text="Add New Product", command=add_product_clicked)
add_product_button.pack(pady=20, padx=20, fill='x')
edit_product_button = Button(product_buttons_container, text="Edit Selected Product", command=edit_product_clicked)
edit_product_button.pack(pady=20, padx=20, fill='x')
delete_product_button = Button(product_buttons_container, text="Delete Selected Product", command=delete_product_clicked)
delete_product_button.pack(pady=20, padx=20, fill='x')
product_bottom_container.lower()

details_form_cover = Frame(product_bottom_container)
details_form_cover.place(relheight=1, relwidth=.8, relx=.2)

new_product_details_form = Frame(product_bottom_container)
new_product_details_form.place(relheight=1, relwidth=.77, relx=.23)
product_title = Label(new_product_details_form, text="Enter the details for the new product:", font=('Arial 12'))
product_title.grid(row=0, column=0, columnspan=2, pady=13)
supplier_id_label = Label(new_product_details_form, text="Supplier ID:")
supplier_id_label.grid(row=1, column=0, pady=10, padx=10)
supplier_id_entry_new = Entry(new_product_details_form, width=75)
supplier_id_entry_new.grid(row=1, column=1, pady=10, padx=10)
product_name_label = Label(new_product_details_form, text="Product Name:")
product_name_label.grid(row=2, column=0, pady=10, padx=10)
product_name_entry_new = Entry(new_product_details_form, width=75)
product_name_entry_new.grid(row=2, column=1, pady=10, padx=10)
manufacturer_label = Label(new_product_details_form, text="Manufacturer:")
manufacturer_label.grid(row=3, column=0, pady=10, padx=10)
manufacturer_entry_new = Entry(new_product_details_form, width=75)
manufacturer_entry_new.grid(row=3, column=1, pady=10, padx=10)
ppc_label = Label(new_product_details_form, text="Price per Case:")
ppc_label.grid(row=4, column=0, pady=10, padx=10)
ppc_entry_new = Entry(new_product_details_form, width=75)
ppc_entry_new.grid(row=4, column=1, pady=10, padx=10)
case_qty_label = Label(new_product_details_form, text="Quantity in Case:")
case_qty_label.grid(row=5, column=0, pady=10, padx=10)
case_qty_entry_new = Entry(new_product_details_form, width=75)
case_qty_entry_new.grid(row=5, column=1, pady=10, padx=10)
new_product_submit_button = Button(new_product_details_form, text="Submit", width=20, command=submit_new_product)
new_product_submit_button.grid(row=6, column=1)
new_product_details_form.lower()

edit_product_details_form = Frame(product_bottom_container)
edit_product_details_form.place(relheight=1, relwidth=.77, relx=.23)
product_title = Label(edit_product_details_form, text="Edit details for existing product:", font=('Arial 12'))
product_title.grid(row=0, column=0, columnspan=2, pady=13)
supplier_id_label = Label(edit_product_details_form, text="Supplier ID:")
supplier_id_label.grid(row=1, column=0, pady=10, padx=10)
supplier_id_entry = Entry(edit_product_details_form, width=75)
supplier_id_entry.grid(row=1, column=1, pady=10, padx=10)
product_name_label = Label(edit_product_details_form, text="Product Name:")
product_name_label.grid(row=2, column=0, pady=10, padx=10)
product_name_entry = Entry(edit_product_details_form, width=75)
product_name_entry.grid(row=2, column=1, pady=10, padx=10)
manufacturer_label = Label(edit_product_details_form, text="Manufacturer:")
manufacturer_label.grid(row=3, column=0, pady=10, padx=10)
manufacturer_entry = Entry(edit_product_details_form, width=75)
manufacturer_entry.grid(row=3, column=1, pady=10, padx=10)
ppc_label = Label(edit_product_details_form, text="Price per Case:")
ppc_label.grid(row=4, column=0, pady=10, padx=10)
ppc_entry = Entry(edit_product_details_form, width=75)
ppc_entry.grid(row=4, column=1, pady=10, padx=10)
case_qty_label = Label(edit_product_details_form, text="Quantity in Case:")
case_qty_label.grid(row=5, column=0, pady=10, padx=10)
case_qty_entry = Entry(edit_product_details_form, width=75)
case_qty_entry.grid(row=5, column=1, pady=10, padx=10)
product_id_label1 = Label(edit_product_details_form, text="Product ID:")
product_id_label1.grid(row=6, column=0, pady=10, padx=10)
product_id_text = StringVar()
product_id_label2 = Label(edit_product_details_form, textvariable=product_id_text)
product_id_label2.grid(row=6, column=1, pady=10, padx=10)
edit_product_submit_button = Button(edit_product_details_form, text="Submit", width=20, command=edit_product_submit)
edit_product_submit_button.grid(row=7, column=1)
edit_product_details_form.lower()

confirm_delete_product = Frame(product_bottom_container)
confirm_delete_product.place(relheight=1, relwidth=.77, relx=.23)
delete_text = Label(confirm_delete_product, text="Are you sure you want to delete this item?", font=('Helvetica 20 bold'))
delete_text.pack(anchor='n', pady=40)
delete_warning = Label(confirm_delete_product, text="Warning: This action cannot be undone!", font=('Helvetica 10'), fg='red')
delete_warning.pack(anchor='n', pady=10)
confirm_delete_button = Button(confirm_delete_product, text="DELETE", command=confirm_delete_clicked, width=10)
confirm_delete_button.place(relx=.28, rely=.5)
cancel_delete_button = Button(confirm_delete_product, text="Cancel", command=confirm_delete_product.lower(), width=10)
cancel_delete_button.place(relx=.58, rely=.5)
confirm_delete_product.lower()
#end products

#being suppliers
suppliers_main_frame = Frame(inventory_data_container)
suppliers_main_frame.place(relwidth=1, relheight=1)
suppliers_list_frame = Frame(suppliers_main_frame)
suppliers_list_frame.place(relwidth=1, relheight=.5)

suppliers_tree = ttk.Treeview(suppliers_list_frame)
suppliers_tree['show'] = 'headings'
suppliers_tree['columns'] = ("Supplier ID", "Supplier Name", "Phone Number", "Email", "State ID", "County")
suppliers_tree.pack(fill='x')
suppliers_main_frame.lower()
suppliers_tree.column("Supplier ID", width=10, anchor='center')
suppliers_tree.column("Supplier Name", width=10, anchor='center')
suppliers_tree.column("Phone Number", width=10, anchor='center')
suppliers_tree.column("Email", width=10, anchor='center')
suppliers_tree.column("State ID", width=10, anchor='center')
suppliers_tree.column("County", width=10, anchor='center')
suppliers_tree.heading("Supplier ID", text="Supplier ID")
suppliers_tree.heading("Supplier Name", text="Supplier Name")
suppliers_tree.heading("Phone Number", text="Phone Number")
suppliers_tree.heading("Email", text="Email")
suppliers_tree.heading("State ID", text="State ID")
suppliers_tree.heading("County", text="County")

suppliers_bottom_frame = Frame(suppliers_main_frame)
suppliers_bottom_frame.place(relwidth=1, relheight=.65, rely=.35)
suppliers_buttons_frame = Frame(suppliers_bottom_frame)
suppliers_buttons_frame.place(relwidth=.3, relheight=1)

suppliers_buttons_container = Frame(suppliers_buttons_frame)
suppliers_buttons_container.place(relwidth=.8, relx=.1, relheight=.6, rely=.2)
add_supplier_button = Button(suppliers_buttons_container, text="Add New Supplier", command=add_new_supplier, pady=5)
add_supplier_button.pack(fill=X, pady=15)
edit_supplier_button = Button(suppliers_buttons_container, text="Edit Selected Supplier", command=edit_supplier, pady=5)
edit_supplier_button.pack(fill=X, pady=15)
delete_supplier_button = Button(suppliers_buttons_container, text="Delete Selected Supplier", command=delete_supplier, pady=5) 
delete_supplier_button.pack(fill=X, pady=15)

suppliers_data_frame = Frame(suppliers_bottom_frame)
suppliers_data_frame.place(relheight=1, relwidth=.7, relx=.3)
suppliers_data_frame_cover = Frame(suppliers_data_frame)
suppliers_data_frame_cover.place(relheight=1, relwidth=1)

s.configure('Tlabel', font=('Arial', 12))
new_supplier_entry = Frame(suppliers_data_frame)
new_supplier_entry.place(relheight=1, rely=.07, relwidth=.7, relx=.15)
new_supplier_head = Label(new_supplier_entry, text="Enter the new supplier details:", font=('Arial 14'))
new_supplier_head.grid(row=0, column=0, columnspan=2, pady=20, padx=10)
new_supplier_name_label = ttk.Label(new_supplier_entry, text="Supplier Name")
new_supplier_name_label.grid(row=1, column=0, pady=10, padx=10, sticky=W)
new_supplier_name_entry = Entry(new_supplier_entry, width=50)
new_supplier_name_entry.grid(row=1, column=1, pady=10, padx=10)
new_supplier_phone_label = Label(new_supplier_entry, text="Phone Number")
new_supplier_phone_label.grid(row=2, column=0, pady=10, padx=10, sticky=W)
new_supplier_phone_entry = Entry(new_supplier_entry, width=50)
new_supplier_phone_entry.grid(row=2, column=1, pady=10, padx=10)
new_supplier_email_label = Label(new_supplier_entry, text="Email")
new_supplier_email_label.grid(row=3, column=0, pady=10, padx=10, sticky=W)
new_supplier_email_entry = Entry(new_supplier_entry, width=50)
new_supplier_email_entry.grid(row=3, column=1, pady=10, padx=10)
new_supplier_stateid_label = Label(new_supplier_entry, text="State ID")
new_supplier_stateid_label.grid(row=4, column=0, pady=10, padx=10, sticky=W)
new_supplier_stateid_entry = Entry(new_supplier_entry, width=50)
new_supplier_stateid_entry.grid(row=4, column=1, pady=10, padx=10)
new_supplier_county_label = Label(new_supplier_entry, text="County")
new_supplier_county_label.grid(row=5, column=0, pady=10, padx=10, sticky=W)
new_supplier_county_entry = Entry(new_supplier_entry, width=50)
new_supplier_county_entry.grid(row=5, column=1, pady=10, padx=10)
new_supplier_submit = Button(new_supplier_entry, text="Submit", command=new_supplier_submitted)
new_supplier_submit.grid(row=6, column=1, pady=10, padx=10)
new_supplier_entry.lower()

edit_supplier_entry = Frame(suppliers_data_frame)
edit_supplier_entry.place(relheight=1, rely=.07, relwidth=.7, relx=.15)
edit_supplier_head = Label(edit_supplier_entry, text="Edit the supplier details:", font=('Arial 14'))
edit_supplier_head.grid(row=0, column=0, columnspan=2, pady=20, padx=10)
edit_supplier_name_label = ttk.Label(edit_supplier_entry, text="Supplier Name")
edit_supplier_name_label.grid(row=1, column=0, pady=10, padx=10, sticky=W)
edit_supplier_name_entry = Entry(edit_supplier_entry, width=50)
edit_supplier_name_entry.grid(row=1, column=1, pady=10, padx=10)
edit_supplier_phone_label = Label(edit_supplier_entry, text="Phone Number")
edit_supplier_phone_label.grid(row=2, column=0, pady=10, padx=10, sticky=W)
edit_supplier_phone_entry = Entry(edit_supplier_entry, width=50)
edit_supplier_phone_entry.grid(row=2, column=1, pady=10, padx=10)
edit_supplier_email_label = Label(edit_supplier_entry, text="Email")
edit_supplier_email_label.grid(row=3, column=0, pady=10, padx=10, sticky=W)
edit_supplier_email_entry = Entry(edit_supplier_entry, width=50)
edit_supplier_email_entry.grid(row=3, column=1, pady=10, padx=10)
edit_supplier_stateid_label = Label(edit_supplier_entry, text="State ID")
edit_supplier_stateid_label.grid(row=4, column=0, pady=10, padx=10, sticky=W)
edit_supplier_stateid_entry = Entry(edit_supplier_entry, width=50)
edit_supplier_stateid_entry.grid(row=4, column=1, pady=10, padx=10)
edit_supplier_county_label = Label(edit_supplier_entry, text="County")
edit_supplier_county_label.grid(row=5, column=0, pady=10, padx=10, sticky=W)
edit_supplier_county_entry = Entry(edit_supplier_entry, width=50)
edit_supplier_county_entry.grid(row=5, column=1, pady=10, padx=10)
edit_supplier_supid_label = Label(edit_supplier_entry, text="Supplier ID")
edit_supplier_supid_label.grid(row=6, column=0, pady=10, padx=10, sticky=W)
sup_id = StringVar()
edit_supplier_supid_label2 = Label(edit_supplier_entry, textvariable=sup_id)
edit_supplier_supid_label2.grid(row=6, column=1, pady=10, padx=10)
edit_supplier_submit = Button(edit_supplier_entry, text="Submit", command=edit_supplier_submitted)
edit_supplier_submit.grid(row=7, column=1, pady=10, padx=10)
edit_supplier_entry.lower()

delete_supplier_data = Frame(suppliers_data_frame)
delete_supplier_data.place(relheight=1, relwidth=1)
delete_text = Label(delete_supplier_data, text="Are you sure you want to delete this item?", font=('Helvetica 20 bold'))
delete_text.pack(anchor='n', pady=40)
delete_warning = Label(delete_supplier_data, text="Warning: This action cannot be undone!", font=('Helvetica 10'), fg='red')
delete_warning.pack(anchor='n', pady=10)
confirm_delete_button = Button(delete_supplier_data, text="DELETE", command=confirm_supplier_delete_clicked, width=10)
confirm_delete_button.place(relx=.28, rely=.5)
cancel_delete_button = Button(delete_supplier_data, text="Cancel", command=delete_supplier_data.lower, width=10)
cancel_delete_button.place(relx=.58, rely=.5)
error_label = Label(delete_supplier_data, text="ERROR! Can't delete because there are products from this supplier in your system. \n Delete the products first and try again.", fg='red')
delete_supplier_data.lower()
update_suppliers()
#end suppliers

#begin counts
counts_main_frame = Frame(inventory_data_container)
counts_main_frame.place(relwidth=1, relheight=1)
counts_head_frame = Frame(counts_main_frame)
counts_head_frame.place(relwidth=1, relheight=.2)
counts_header = Label(counts_head_frame, text="Select a store ID below to update the inventory counts:", font=('Helvetica 12 bold'))
counts_header.pack(pady=10)
counts_cb_svar = StringVar()
counts_cb_svar.set("")
counts_cb = ttk.Combobox(counts_head_frame, textvariable=counts_cb_svar, values=all_stores, state='readonly')
counts_cb.pack(fill='x')
counts_cb.bind("<<ComboboxSelected>>", cb_store_selected)
counts_header2 = Label(counts_head_frame, text="Select a product category:", font=('Helvetica 12 bold'))
counts_svar = StringVar()
counts_svar.set("")
counts_products_cb = ttk.Combobox(counts_head_frame, textvariable=counts_svar, values=options, state='readonly')
counts_products_cb.bind("<<ComboboxSelected>>", cb_product_type_selected)
counts_main_frame.lower()
counts_data = Frame(counts_main_frame)
counts_data.place(relwidth=1, relheight=.8, rely=.2)
counts_data.lower()
#end counts



#END INVENTORY TAB

#BEGIN ORDERS TAB
admin_notebook.add(admin_orders_frame, text="Orders")
orders_button_container = Frame(admin_orders_frame, bg='grey')
orders_button_container.pack(side="left", fill="y")
view_orders_button = Button(orders_button_container, text="View Orders", command=view_orders_clicked)
view_orders_button.pack(pady=10, fill=X)
create_order_button = Button(orders_button_container, text="Create New Order", command=create_order_clicked)
create_order_button.pack(pady=10, fill=X)
delete_order_button = Button(orders_button_container, text="Cancel/Delete Order", command=delete_cancel_order_clicked)
delete_order_button.pack(pady=10, fill=X)
view_invoices_button = Button(orders_button_container, text="View Invoices\nand Payments", command=view_invoices_clicked)
view_invoices_button.pack(pady=10, fill=X)
orders_data_container = Frame(admin_orders_frame)
orders_data_container.pack(fill='both', expand=True)

orders_main_frame = Frame(orders_data_container)
orders_main_frame.place(relwidth=1, relheight=1)
orders_frame_message = Label(orders_main_frame, text="Please select an option from the left", font=('Helvetica 20 bold'))
orders_frame_message.place(relx=.25, rely=.3)

#begin view orders
view_orders_main_frame = Frame(orders_data_container)
view_orders_main_frame.place(relwidth=1, relheight=1)
view_orders_header = PanedWindow(view_orders_main_frame)
view_orders_header.place(relwidth=1, relheight=.18)
view_orders_header_data = Frame(view_orders_header)
view_orders_header_data.pack(anchor=N)
select_orders_header_label = Label(view_orders_header_data, text="Please choose from the options below to view existing orders", font=('Helvetica 12 bold'))
select_orders_header_label.grid(column=0, row=0, columnspan=3, sticky=N)
select_orders_store_label = Label(view_orders_header_data, text="Select a store ID:")
select_orders_store_label.grid(row=1, column=0)
orderstores_svar = StringVar()
orderstores_svar.set("All Stores")
orders_stores_cb = ttk.Combobox(view_orders_header_data, textvariable=orderstores_svar, values=stores_with_all, state='readonly', width=30)
orders_stores_cb.grid(row=2, column=0)
select_orders_sup_label = Label(view_orders_header_data, text="Select a supplier ID:")
select_orders_sup_label.grid(row=3, column=0)
ordersups_svar = StringVar()
ordersups_svar.set("All Suppliers")
orders_sups_cb = ttk.Combobox(view_orders_header_data, textvariable=ordersups_svar, values=all_sups, state='readonly', width=30)
orders_sups_cb.grid(row=4, column=0)
order_var = StringVar()
order_var.set('placed_and_received')
r1 = Radiobutton(view_orders_header_data, text='Orders Placed & Received', variable=order_var, value='placed_and_received')
r1.grid(row=2, column=1, sticky=W, padx=15)
r2 = Radiobutton(view_orders_header_data, text='Orders Placed, not yet received', variable=order_var, value='placed')
r2.grid(row=3, column=1, sticky=W, padx=15)
r3 = Radiobutton(view_orders_header_data, text='Both', variable=order_var, value='both')
r3.grid(row=4, column=1, sticky=W, padx=15)
get_orders_button = Button(view_orders_header_data, text="GET ORDERS", width=20, command=get_orders_clicked)
get_orders_button.grid(column=2, row=3, sticky=NSEW, padx=15)

orders_bottom_container = Frame(view_orders_main_frame)
orders_bottom_container.place(relwidth=1, relheight=.82, rely=.18)
orders_tree_container= Frame(orders_bottom_container)
orders_tree_container.place(relwidth=.48, relx=.003, relheight=1)
orders_tree = ttk.Treeview(orders_tree_container)
orders_tree['show'] = 'headings'
orders_tree['columns'] = ('Order ID', 'Supplier ID', 'Store ID', 'Date Placed', 'Date Received')
orders_tree.pack(fill=BOTH, expand=YES)
orders_tree.column("Order ID", width=10, anchor='center')
orders_tree.column("Supplier ID", width=10, anchor='center')
orders_tree.column("Store ID", width=10, anchor='center')
orders_tree.column("Date Placed", width=10, anchor='center')
orders_tree.column("Date Received", width=10, anchor='center')
orders_tree.heading("Order ID", text="Order ID")
orders_tree.heading("Supplier ID", text="Supplier ID")
orders_tree.heading("Store ID", text="Store ID")
orders_tree.heading("Date Placed", text="Date Placed")
orders_tree.heading("Date Received", text="Date Received")
orders_tree.bind("<<TreeviewSelect>>", order_selected)

orders_details_container = Frame(orders_bottom_container)
orders_details_container.place(relheight=1, relwidth=.48, relx=.518)
order_dets_tree_container = Frame(orders_details_container)
order_dets_tree_container.place(relheight=.6, relwidth=1)
orders_details_tree = ttk.Treeview(order_dets_tree_container)
orders_details_tree['show'] = 'headings'
orders_details_tree['columns'] = ('Product', 'Price Per Case', 'Cases Ordered', 'Total Cost')
orders_details_tree.pack(fill=BOTH, expand=YES)
orders_details_tree.column("Product", width=10, anchor='w')
orders_details_tree.column("Price Per Case", width=10, anchor='center')
orders_details_tree.column("Cases Ordered", width=10, anchor='center')
orders_details_tree.column("Total Cost", width=10, anchor='center')
orders_details_tree.heading("Product", text="Product")
orders_details_tree.heading("Price Per Case", text="Price Per Case")
orders_details_tree.heading("Cases Ordered", text="Cases Ordered")
orders_details_tree.heading("Total Cost", text="Total Cost")
edit_rec_date_container = Frame(orders_details_container, bg='white', highlightthickness=.5, highlightbackground='grey')
edit_rec_date_container.place(relwidth=1, relheight=.38, rely=.61)
edit_rec_date_data = Frame(edit_rec_date_container, bg='white')
edit_rec_date_data.pack(anchor=N)
edit_dates_header = Label(edit_rec_date_data, bg='white', text="EDIT DATE DETAILS FOR SELECTED ORDER:", font=("Arial 10 bold"))
edit_dates_header.grid(row=0, column=0, columnspan=2, pady=10)
edit_place_date_label = Label(edit_rec_date_data, bg='white', text="Date Placed: ")
edit_place_date_label.grid(row=1, column=0, pady=10)
sv_dateplaced = StringVar()
edit_place_date_entry = Entry(edit_rec_date_data, bg='white')
edit_place_date_entry.grid(row=1, column=1, pady=10)
edit_rec_date_label = Label(edit_rec_date_data, bg='white', text="Date Received: ")
edit_rec_date_label.grid(row=2, column=0, pady=10)
sv_daterec = StringVar()
edit_rec_date_entry = Entry(edit_rec_date_data, bg='white')
edit_rec_date_entry.grid(row=2, column=1, pady=10)
edit_rec_submit_button = Button(edit_rec_date_data, text="SUBMIT CHANGES", command=submit_date_changes, state=DISABLED)
edit_rec_submit_button.grid(row=3, column=0, columnspan=2)
view_orders_main_frame.lower()
#end view orders

#begin create new order
create_order_main_frame = Frame(orders_data_container)
create_order_main_frame.place(relwidth=1, relheight=1)
create_order_header = Frame(create_order_main_frame)
create_order_header.place(relwidth=1, relheight=.15)
create_order_header_data = Frame(create_order_header)
create_order_header_data.pack(anchor=N)
create_order_header_label = Label(create_order_header_data, text="Enter details below to create a new order", font=('Helvetica 12 bold'), pady=10)
create_order_header_label.grid(row=0, column=0, columnspan=8)
store_label = Label(create_order_header_data, text="Select A Store:")
store_label.grid(row=1, column=0, padx=5)
cb_store = StringVar()
cb_store.set("")
cb_new_order_store = ttk.Combobox(create_order_header_data, textvariable=cb_store, values=all_stores, state="readonly", width=5)
cb_new_order_store.grid(row=1, column=1, padx=5)
sup_label = Label(create_order_header_data, text="Select A Supplier:")
sup_label.grid(row=1, column=2, padx=5)
cb_sup = StringVar()
cb_sup.set("")
cb_new_order_sup = ttk.Combobox(create_order_header_data, textvariable=cb_sup, values=sups, state="readonly", width=5)
cb_new_order_sup.grid(row=1, column=3, padx=5)
date_placed_label = Label(create_order_header_data, text="Date Placed:")
date_placed_label.grid(row=1, column=4, padx=5)
date_placed_entry = Entry(create_order_header_data)
date_placed_entry.insert(0, "MM/DD/YYYY")
date_placed_entry.grid(row=1, column=5, padx=5)
date_received_label = Label(create_order_header_data, text="Date Received:")
date_received_label.grid(row=1, column=6)
date_received_entry = Entry(create_order_header_data)
date_received_entry.insert(0, "")
date_received_entry.grid(row=1, column=7, padx=5)
payment_due_date = Label(create_order_header_data, text="Payment to Supplier Due Date:")
payment_due_date.grid(row=2, column=0, columnspan=2, padx=5)
payment_due_date_entry = Entry(create_order_header_data)
payment_due_date_entry.grid(row=2, column=2, padx=5)
start_order_button = Button(create_order_header_data, text="START ORDER", command=start_order, width=15)
start_order_button.grid(row=2, column=3, columnspan=3, pady=10)

new_order_bottom_container = Frame(create_order_main_frame)
new_order_bottom_container.place(relwidth=1, relheight=.85, rely=.15)
bottom_buttons_container = Frame(new_order_bottom_container)
bottom_buttons_container.place(relwidth=1, relheight=.1, rely=.9)
bottom_buttons_cover = Frame(new_order_bottom_container)
bottom_buttons_cover.place(relwidth=1, relheight=.1, rely=.9)
order_buttons = Frame(bottom_buttons_container)
order_buttons.pack(anchor=S)
order_submit = Button(order_buttons, text="Create Order", command=submit_order_clicked)
order_submit.grid(row=0, column=0, pady=20, padx=10)
order_cancel = Button(order_buttons, text="Cacel Order", command=cancel_order_clicked)
order_cancel.grid(row=0, column=1, pady=20, padx=10)
bottom_buttons_container.lower()
create_order_main_frame.lower()
#end create new order

#begin delete order
delete_order_main_frame = Frame(orders_data_container)
delete_order_main_frame.place(relwidth=1, relheight=1)
delete_order_header = Frame(delete_order_main_frame)
delete_order_header.place(relwidth=1, relheight=.2)
delete_order_header_data = Frame(delete_order_header)
delete_order_header_data.pack(anchor=N)
delete_order_header_label = Label(delete_order_header_data, text="Select order details below.", font=("Helvetica 12 bold"))
delete_order_header_label.grid(row=0, column=0, columnspan=4)
delete_order_header_label2 = Label(delete_order_header_data, text="(Please note: you can only cancel or delete orders that have no recorded payments AND have not been marked as received)", font=("Helvetica 10"))
delete_order_header_label2.grid(row=1, column=0, columnspan=4, pady=10)
delete_order_store_label = Label(delete_order_header_data, text="Select a Store ID:")
delete_order_store_label.grid(row=2, column=0, padx=10)
delete_order_store_cb = ttk.Combobox(delete_order_header_data, textvariable=orderstores_svar, values=stores_with_all, state='readonly', width=30)
delete_order_store_cb.grid(row=2, column=1, padx=10)
delete_order_sup_label = Label(delete_order_header_data, text="Select a Supplier ID:")
delete_order_sup_label.grid(row=2, column=2, padx=10)
delete_order_sup_cb = ttk.Combobox(delete_order_header_data, textvariable=ordersups_svar, values=all_sups, state='readonly', width=30)
delete_order_sup_cb.grid(row=2, column=3, padx=10)
delete_orders_view_button = Button(delete_order_header_data, text="VIEW ORDERS", command=delete_order_view_orders)
delete_orders_view_button.grid(row=3, column=0, columnspan=4, pady=10)

delete_order_tree_container = Frame(delete_order_main_frame)
delete_order_tree_container.place(relheight=.5, relwidth=1, rely=.2)
delete_order_tree = ttk.Treeview(delete_order_tree_container)
delete_order_tree.pack(fill=BOTH, expand=YES)
delete_order_tree['show'] = 'headings'
delete_order_tree['columns'] = ('Order ID', 'Store ID', 'Date Placed', 'Date Received', 'Amount Due', 'Amount Paid')
delete_order_tree.column("Order ID", width=5)
delete_order_tree.column("Store ID", width=5)
delete_order_tree.column("Date Placed", width=10)
delete_order_tree.column("Date Received", width=10)
delete_order_tree.column("Amount Due", width=10)
delete_order_tree.column("Amount Paid", width=10)

delete_order_tree.heading("Order ID", text="Order ID")
delete_order_tree.heading("Store ID", text="Store ID")
delete_order_tree.heading("Date Placed", text="Date Placed")
delete_order_tree.heading("Date Received", text="Date Received")
delete_order_tree.heading("Amount Due", text="Amount Due")
delete_order_tree.heading("Amount Paid", text="Amound Paid")
delete_order_tree.bind("<<TreeviewSelect>>", del_order_tree_selected)

delete_order_bottom_container = Frame(delete_order_main_frame)
delete_order_bottom_container.place(relwidth=1, relheight=.3, rely=.7)
delete_order_button_container = Frame(delete_order_bottom_container)
delete_order_button_container.pack(anchor=N)
mark_as_canceled_button = Button(delete_order_button_container, text="Mark Selected Order as Canceled", command=mark_as_canceled_clicked, state=DISABLED)
mark_as_canceled_button.grid(row=0, column=0, pady=20, padx=10)
delete_order_button = Button(delete_order_button_container, text="DELETE SELECTED ORDER", command=delete_order_clicked, state=DISABLED)
delete_order_button.grid(row=0, column=1, pady=20)

warning_message_cover = Frame(delete_order_bottom_container)
warning_message_cover.place(relwidth=1, relheight=.7, rely=.3)
warning_message_cancel = Frame(delete_order_bottom_container)
warning_message_cancel.place(relwidth=1, relheight=.7, rely=.3)
cancel_message = Label(warning_message_cancel, text="Are you sure you want to mark this order as canceled? This action cannot be undone.", font=("Arial 11 bold"))
cancel_message.pack(anchor=N, pady=15)
cancel_confirm_button = Button(warning_message_cancel, text="CONFIM", command=mark_cancel_cofirmed, width=15)
cancel_confirm_button.pack(anchor=CENTER, pady=5)
cancel_cancel_button = Button(warning_message_cancel, text="CANCEL", command=warning_message_cover.lift, width=15)
cancel_cancel_button.pack(anchor=CENTER, pady=5)
warning_message_cancel.lower()

warning_message_del = Frame(delete_order_bottom_container)
warning_message_del.place(relwidth=1, relheight=.7, rely=.3)
cancel_message = Label(warning_message_del, text="Are you sure you want to completely remove this order from your system?\nThis action cannot be undone", font=("Arial 11 bold"))
cancel_message.pack(anchor=N, pady=15)
cancel_confirm_button = Button(warning_message_del, text="CONFIM", command=mark_del_cofirmed, width=15)
cancel_confirm_button.pack(anchor=CENTER, pady=5)
cancel_cancel_button = Button(warning_message_del, text="CANCEL", command=warning_message_cover.lift, width=15)
cancel_cancel_button.pack(anchor=CENTER, pady=5)
warning_message_del.lower()

delete_order_main_frame.lower()
#end delete order

#begin invoices
invoices_main_frame = Frame(orders_data_container)
invoices_main_frame.place(relwidth=1, relheight=1)
invoices_header = PanedWindow(invoices_main_frame)
invoices_header.place(relwidth=1, relheight=.18)
invoices_header_data = Frame(invoices_header)
invoices_header_data.pack(anchor=N)
invoices_header_label = Label(invoices_header_data, text="Please choose from the options below to view existing invoices", font=('Helvetica 12 bold'))
invoices_header_label.grid(column=0, row=0, columnspan=3, sticky=N)
inv_select_orders_store_label = Label(view_orders_header_data, text="Select a store ID:")
inv_select_orders_store_label.grid(row=1, column=0)
inv_stores_cb = ttk.Combobox(invoices_header_data, textvariable=orderstores_svar, values=stores_with_all, state='readonly', width=30)
inv_stores_cb.grid(row=2, column=0)
inv_sup_label = Label(invoices_header_data, text="Select a supplier ID:")
inv_sup_label.grid(row=3, column=0)
inv_sups_cb = ttk.Combobox(invoices_header_data, textvariable=ordersups_svar, values=all_sups, state='readonly', width=30)
inv_sups_cb.grid(row=4, column=0)
inv_var = StringVar()
inv_var.set('both')
inv_r1 = Radiobutton(invoices_header_data, text='Balance Outstanding', variable=inv_var, value='outstanding')
inv_r1.grid(row=2, column=1, sticky=W, padx=15)
inv_r2 = Radiobutton(invoices_header_data, text='Balance Paid', variable=inv_var, value='paid')
inv_r2.grid(row=3, column=1, sticky=W, padx=15)
inv_r3 = Radiobutton(invoices_header_data, text='Both', variable=inv_var, value='both')
inv_r3.grid(row=4, column=1, sticky=W, padx=15)
get_invoices_button = Button(invoices_header_data, text="GET INVOICES", width=20, command=get_invoices_clicked)
get_invoices_button.grid(column=2, row=3, sticky=NSEW, padx=15)

invoices_data_frame = Frame(invoices_main_frame)
invoices_data_frame.place(relwidth=1, relheight=.82, rely=.18)
invoices_tree_frame = Frame(invoices_data_frame)
invoices_tree_frame.place(relwidth=.6, relheight=1, relx=.01)

invoices_tree = ttk.Treeview(invoices_tree_frame)
invoices_tree['show'] = 'headings'
invoices_tree['columns'] = ('Order ID', 'Store ID', 'Supplier ID', 'Date Placed', 'Total Due', 'Amount Paid')
invoices_tree.pack(fill=BOTH, expand=YES)
invoices_tree.column("Order ID", width=10, anchor='center')
invoices_tree.column("Store ID", width=10, anchor='center')
invoices_tree.column("Supplier ID", width=10, anchor='center')
invoices_tree.column("Date Placed", width=10, anchor='center')
invoices_tree.column("Total Due", width=10, anchor='center')
invoices_tree.column("Amount Paid", width=10, anchor='center')
invoices_tree.heading("Order ID", text="Order ID")
invoices_tree.heading("Store ID", text="Store ID")
invoices_tree.heading("Supplier ID", text="Supplier ID")
invoices_tree.heading("Date Placed", text="Date Placed")
invoices_tree.heading("Total Due", text="Total Due")
invoices_tree.heading("Amount Paid", text="Amount Paid")
invoices_tree.bind("<<TreeviewSelect>>", invoice_selected)

invoices_side_data_container = Frame(invoices_data_frame)
invoices_side_data_container.place(relwidth=.38, relheight=1, relx=.62)
invoices_buttons_container = Frame(invoices_side_data_container)
invoices_buttons_container.place(relwidth=1, relheight=.1)
invoices_buttons = Frame(invoices_buttons_container)
invoices_buttons.pack(anchor=N)
inv_details_button = Button(invoices_buttons, text="View Details for\n Selected Invoice", command=inv_details_clicked, state=DISABLED)
inv_details_button.grid(row=0, column=0, padx=15)
inv_pmt_button = Button(invoices_buttons, text="Log Payment for\n Select Invoice", command=inv_payment_clicked, state=DISABLED)
inv_pmt_button.grid(row=0, column=1, padx=15)

inv_data_cover = Frame(invoices_side_data_container)
inv_data_cover.place(relwidth=1, relheight=.9, rely=.1)
inv_details_frame = Frame(invoices_side_data_container)
inv_details_frame.place(relwidth=1, relheight=.9, rely=.1)
inv_details_label = Label(inv_details_frame, text="Invoice Details", font=("Helvetica 12 bold"))
inv_details_label.grid(row=0, column=0, columnspan=2)
inv_details_supname = Label(inv_details_frame, text="Supplier Name:")
inv_details_supname.grid(row=1, column=0, sticky=W)
inv_supname = StringVar()
inv_supname.set("")
inv_details_supname_data = Label(inv_details_frame, textvariable=inv_supname)
inv_details_supname_data.grid(row=1, column=1, padx=10, sticky=W)
inv_details_date_placed = Label(inv_details_frame, text="Date Placed:")
inv_details_date_placed.grid(row=2, column=0, sticky=W)
inv_date_placed = StringVar()
inv_date_placed.set("")
inv_details_date_placed_data = Label(inv_details_frame, textvariable=inv_date_placed)
inv_details_date_placed_data.grid(row=2, column=1, sticky=W, padx=10)
inv_details_date_rec = Label(inv_details_frame, text="Date Received:")
inv_details_date_rec.grid(row=3, column=0, sticky=W)
inv_date_rec = StringVar()
inv_date_rec.set("N/A")
inv_details_date_rec_data = Label(inv_details_frame, textvariable=inv_date_rec)
inv_details_date_rec_data.grid(row=3, column=1, sticky=W, padx=10)
inv_details_items = Label(inv_details_frame, text="Total Items Ordered:")
inv_details_items.grid(row=4, column=0, sticky=W)
inv_items = StringVar()
inv_items.set("")
inv_details_items_data = Label(inv_details_frame, textvariable=inv_items)
inv_details_items_data.grid(row=4, column=1, sticky=W, padx=10)
payment_details_header = Label(inv_details_frame, text="Payment Details", pady=15, font=("Helvetica 12 bold"))
payment_details_header.grid(row=5, column=0, columnspan=2)
payment_details_id = Label(inv_details_frame, text="Payment ID:")
payment_details_id.grid(row=6, column=0, sticky=W)
payment_id = StringVar()
payment_id.set("N/A")
payment_details_id_data = Label(inv_details_frame, textvariable=payment_id)
payment_details_id_data.grid(row=6, column=1, sticky=W, padx=10)
payment_amount = Label(inv_details_frame, text="Payment Amount:")
payment_amount.grid(row=7, column=0, sticky=W)
pmt_amount = StringVar()
pmt_amount.set("N/A")
payment_amount_data = Label(inv_details_frame, textvariable=pmt_amount)
payment_amount_data.grid(row=7, column=1, sticky=W, padx=10)
payment_date = Label(inv_details_frame, text="Payment Date:")
payment_date.grid(row=8, column=0, sticky=W)
pmt_date = StringVar()
pmt_date.set("N/A")
payment_date_data = Label(inv_details_frame, textvariable=pmt_date)
payment_date_data.grid(row=8, column=1, sticky=W, padx=10)
inv_details_frame.lower()

log_pmt_frame = Frame(invoices_side_data_container)
log_pmt_frame.place(relwidth=1, relheight=.9, rely=.1)
log_pmt_frame_cover = Frame(invoices_side_data_container)
log_pmt_frame_cover.place(relwidth=1, relheight=.9, rely=.1)

log_pmt_paid = Frame(log_pmt_frame)
log_pmt_paid.place(relwidth=1, relheight=1)
already_paid_label = Label(log_pmt_paid, text="This invoice has already been paid!", font="Helvetica 12 bold")
already_paid_label.grid(row=0, column=0)
log_pmt_frame.lower()

log_pmt_details = Frame(log_pmt_frame)
log_pmt_details.place(relwidth=1, relheight=1)
date_paid_label = Label(log_pmt_details, text="Enter the payment date:")
date_paid_label.grid(row=0, column=0, pady=15)
date_paid_entry = Entry(log_pmt_details)
date_paid_entry.grid(row=0, column=1, pady=15)
submit_payment_button = Button(log_pmt_details, text="Submit Payment", command=submit_pmt_clicked)
submit_payment_button.grid(row=1, column=0, pady=15)
cancel_payment_button = Button(log_pmt_details, text="Cancel Payment", command=log_pmt_details.lower)
cancel_payment_button.grid(row=1, column=1, pady=15)
log_pmt_details.lower()

log_pmt_frame.lower()
invoices_main_frame.lower()
#end invoices

#END ORDERS TAB

#BEGIN CATERING TAB
admin_notebook.add(admin_catering_frame, text="Catering")
catering_buttons_container = Frame(admin_catering_frame, bg='grey')
catering_buttons_container.pack(side=LEFT, fill=Y)
catering_customers_button = Button(catering_buttons_container, text="Manage Customers", command=manage_customers_clicked)
catering_customers_button.pack(pady=10, fill=X)
catering_menu_button = Button(catering_buttons_container, text="Manage Catering Menu Items", command=manage_menu_clicked)
catering_menu_button.pack(pady=10, fill=X)
catering_create_event_button = Button(catering_buttons_container, text="Create New Catering Event", command=create_event_clicked)
catering_create_event_button.pack(pady=10, fill=X)
catering_view_events_button = Button(catering_buttons_container, text="View Existing Catering Events", command=view_events_clicked)
catering_view_events_button.pack(pady=10, fill=X)
catering_cancel_event_button = Button(catering_buttons_container, text="Cancel/Delete Event", command=cancel_catering_event_clicked)
catering_cancel_event_button.pack(pady=10, fill=X)
catering_payments_button = Button(catering_buttons_container, text="View Invoices/Payments", command=view_cust_invoices)
catering_payments_button.pack(pady=10, fill=X)

catering_data_container = Frame(admin_catering_frame)
catering_data_container.pack(fill=BOTH, expand=True)

catering_main_frame = Frame(catering_data_container)
catering_main_frame.place(relwidth=1, relheight=1)
catering_frame_message = Label(catering_main_frame, text="Please select an option from the left", font=('Helvetica 20 bold'))
catering_frame_message.place(relx=.25, rely=.3)

#begin manage customers
manage_customers_main_frame = Frame(catering_data_container)
manage_customers_main_frame.place(relwidth=1, relheight=1)
manage_customers_head_container = Frame(manage_customers_main_frame)
manage_customers_head_container.place(relwidth=1, relheight=.04)
manage_customers_head_data = Frame(manage_customers_head_container)
manage_customers_head_data.pack(anchor=N)
manage_customers_header = Label(manage_customers_head_data, text="Existing Customers", font=("Helvetica 12 bold"))
manage_customers_header.pack(anchor=N)

manage_customers_body = Frame(manage_customers_main_frame)
manage_customers_body.place(relwidth=1, relheight=.6, rely=.04)
manage_customers_tree_container = Frame(manage_customers_body)
manage_customers_tree_container.place(relwidth=1, relheight=1)

customers_tree = ttk.Treeview(manage_customers_tree_container)
customers_tree.pack(fill=BOTH, expand=YES)
customers_tree['show'] = 'headings'
customers_tree['columns'] = ('Customer ID', 'First Name', 'Last Name', 'Phone', 'Email')
customers_tree.column("Customer ID", width=5, anchor=N)
customers_tree.column("First Name", width=10)
customers_tree.column("Last Name", width=10)
customers_tree.column("Phone", width=7, anchor=N)
customers_tree.column("Email", width=20)
customers_tree.heading("Customer ID", text="Customer ID")
customers_tree.heading("First Name", text="First Name")
customers_tree.heading("Last Name", text="Last Name")
customers_tree.heading("Phone", text="Phone")
customers_tree.heading("Email", text="Email")
update_customers()


manage_customers_buttons_container = Frame(manage_customers_main_frame)
manage_customers_buttons_container.place(relwidth=1, relheight=.05, rely=.64)
manage_customers_buttons = Frame(manage_customers_buttons_container)
manage_customers_buttons.pack(anchor=N, pady=5)
add_customer_button = Button(manage_customers_buttons, text="Add New Customer", width=30, command=add_new_customer_clicked)
add_customer_button.grid(row=0, column=0, padx=15)
edit_customer_button = Button(manage_customers_buttons, text="Edit Selected Customer", width=30, command=edit_customer_clicked)
edit_customer_button.grid(row=0, column=1, padx=15)
del_customer_button = Button(manage_customers_buttons, text="Delete Selected Customer", width=30, command=del_customer_clicked)
del_customer_button.grid(row=0, column=2, padx=15)

manage_customers_bottom_container = Frame(manage_customers_main_frame)
manage_customers_bottom_container.place(relwidth=1, relheight=.31, rely=.69)
customer_data_cover = Frame(manage_customers_bottom_container)
customer_data_cover.place(relwidth=1, relheight=1)

new_customer_entry_container = Frame(manage_customers_bottom_container)
new_customer_entry_container.place(relwidth=1, relheight=1)
new_customer_data = Frame(new_customer_entry_container)
new_customer_data.pack(anchor=N)
new_customer_header = Label(new_customer_data, text="Please enter customer details below:", font=("Helvetica 10 bold"), pady=15)
new_customer_header.grid(row=0, column=0, columnspan=2)
first_name_label = Label(new_customer_data, text="First Name:")
first_name_label.grid(row=1, column=0, padx=20, sticky=E)
first_name_entry = Entry(new_customer_data, width=30)
first_name_entry.grid(row=1, column=1, padx=20, sticky=E)
last_name_label = Label(new_customer_data, text="Last Name:")
last_name_label.grid(row=2, column=0, padx=20, sticky=E)
last_name_entry = Entry(new_customer_data, width=30)
last_name_entry.grid(row=2, column=1, padx=20, sticky=E)
phone_label = Label(new_customer_data, text="Phone Number:")
phone_label.grid(row=3, column=0, padx=20, sticky=E)
phone_entry = Entry(new_customer_data, width=30)
phone_entry.grid(row=3, column=1, padx=20, sticky=E)
email_label = Label(new_customer_data, text="Email Address:")
email_label.grid(row=4, column=0, padx=20, sticky=E)
email_entry = Entry(new_customer_data, width=30)
email_entry.grid(row=4, column=1, padx=20, sticky=E)
customer_submit_button = Button(new_customer_data, text="Create New Customer", width=20, command=confirm_new_customer_clicked)
customer_submit_button.grid(row=5, column=0, pady=25)
customer_cancel_button = Button(new_customer_data, text="Cancel", command=customer_data_cover.lift, width=20)
customer_cancel_button.grid(row=5, column=1, pady=25)
new_customer_entry_container.lower()

edit_customer_container = Frame(manage_customers_bottom_container)
edit_customer_container.place(relwidth=1, relheight=1)
edit_customer_data = Frame(edit_customer_container)
edit_customer_data.pack(anchor=N)
edit_customer_header = Label(edit_customer_data, text="Please enter customer details below:", font=("Helvetica 10 bold"), pady=15)
edit_customer_header.grid(row=0, column=0, columnspan=2)
efirst_name_label = Label(edit_customer_data, text="First Name:")
efirst_name_label.grid(row=1, column=0, padx=20, sticky=E)
efirst_name_entry = Entry(edit_customer_data, width=30)
efirst_name_entry.grid(row=1, column=1, padx=20, sticky=E)
elast_name_label = Label(edit_customer_data, text="Last Name:")
elast_name_label.grid(row=2, column=0, padx=20, sticky=E)
elast_name_entry = Entry(edit_customer_data, width=30)
elast_name_entry.grid(row=2, column=1, padx=20, sticky=E)
ephone_label = Label(edit_customer_data, text="Phone Number:")
ephone_label.grid(row=3, column=0, padx=20, sticky=E)
ephone_entry = Entry(edit_customer_data, width=30)
ephone_entry.grid(row=3, column=1, padx=20, sticky=E)
eemail_label = Label(edit_customer_data, text="Email Address:")
eemail_label.grid(row=4, column=0, padx=20, sticky=E)
eemail_entry = Entry(edit_customer_data, width=30)
eemail_entry.grid(row=4, column=1, padx=20, sticky=E)
ecid_label = Label(edit_customer_data, text="Customer ID:")
ecid_label.grid(row=5, column=0, padx=20, sticky=E)
e_cid = StringVar()
ecid_label2 = Label(edit_customer_data, textvariable=e_cid)
ecid_label2.grid(row=5, column=1, padx=20, sticky=N)
ecustomer_submit_button = Button(edit_customer_data, text="Submit Changes", width=20, command=confirm_edit_customer_clicked)
ecustomer_submit_button.grid(row=6, column=0, pady=15)
ecustomer_cancel_button = Button(edit_customer_data, text="Cancel", command=customer_data_cover.lift, width=20)
ecustomer_cancel_button.grid(row=6, column=1, pady=15)
edit_customer_container.lower()

delete_customer_container = Frame(manage_customers_bottom_container)
delete_customer_container.place(relwidth=1, relheight=1)

del_customer_cover = Frame(delete_customer_container)
del_customer_cover.place(relwidth=1, relheight=1)

del_customer_error = Frame(delete_customer_container)
del_customer_error.place(relwidth=1, relheight=1)
del_customer_error_label = Label(del_customer_error, text="ERROR! Can't delete a customer that is currently linked to a catering event!", font=("Helvetica 12 bold"), pady=40)
del_customer_error_label.pack(anchor=N)
del_customer_error.lower()

del_customer_label_container = Frame(delete_customer_container)
del_customer_label_container.place(relheight=1, relwidth=1)
del_customer_warning = Frame(del_customer_label_container)
del_customer_warning.pack(anchor=N)
del_customer_warning_label = Label(del_customer_warning, text="Are you sure you want to delete this customer?", font=("Helvetica 12 bold"))
del_customer_warning_label.grid(row=0, column=0, pady=20, columnspan=2)
del_customer_warning_label2 = Label(del_customer_warning, text="WARNING: This action is PERMANENT and cannot be undone!", font=("Helvetica 10"), fg='red')
del_customer_warning_label2.grid(row=1, column=0, columnspan=2, pady=10)
del_customer_confirm_button = Button(del_customer_warning, text="CONFIRM DELETE", command=delete_customer_confirmed)
del_customer_confirm_button.grid(row=2, column=0, padx=20)
del_customer_cancel_button = Button(del_customer_warning, text="Cancel", command=customer_data_cover.lift)
del_customer_cancel_button.grid(row=2, column=1, padx=20)
del_customer_warning.lower()
delete_customer_container.lower()

manage_customers_main_frame.lower()
#end manage customers

#begin manage menu
manage_menu_main_frame = Frame(catering_data_container)
manage_menu_main_frame.place(relwidth=1, relheight=1)
manage_menu_head_container = Frame(manage_menu_main_frame)
manage_menu_head_container.place(relwidth=1, relheight=.04)
manage_menu_head_data = Frame(manage_menu_head_container)
manage_menu_head_data.pack(anchor=N)
manage_menu_header = Label(manage_menu_head_data, text="Current menu items available for catering events", font=("Helvetica 12 bold"))
manage_menu_header.pack(anchor=N)

manage_menu_body = Frame(manage_menu_main_frame)
manage_menu_body.place(relwidth=1, relheight=.6, rely=.04)
manage_menu_tree_container = Frame(manage_menu_body)
manage_menu_tree_container.place(relwidth=1, relheight=1)

menu_tree = ttk.Treeview(manage_menu_tree_container)
menu_tree.pack(fill=BOTH, expand=YES)
menu_tree['show'] = 'headings'
menu_tree['columns'] = ('Menu Item ID', 'Item Name', 'Price')
menu_tree.column("Menu Item ID", width=5, anchor=N)
menu_tree.column("Item Name", width=10, anchor=W)
menu_tree.column("Price", width=10, anchor=N)
menu_tree.heading("Menu Item ID", text="Menu Item ID")
menu_tree.heading("Item Name", text="Item Name")
menu_tree.heading("Price", text="Price")
update_menu()


manage_menu_buttons_container = Frame(manage_menu_main_frame)
manage_menu_buttons_container.place(relwidth=1, relheight=.05, rely=.64)
manage_menu_buttons = Frame(manage_menu_buttons_container)
manage_menu_buttons.pack(anchor=N, pady=5)
add_menu_button = Button(manage_menu_buttons, text="Add New Menu Item", width=30, command=add_new_menu_clicked)
add_menu_button.grid(row=0, column=0, padx=15)
edit_menu_button = Button(manage_menu_buttons, text="Edit Selected Menu Item", width=30, command=edit_menu_clicked)
edit_menu_button.grid(row=0, column=1, padx=15)
del_menu_button = Button(manage_menu_buttons, text="Delete Selected Menu Item", width=30, command=del_menu_clicked)
del_menu_button.grid(row=0, column=2, padx=15)

manage_menu_bottom_container = Frame(manage_menu_main_frame)
manage_menu_bottom_container.place(relwidth=1, relheight=.31, rely=.69)
menu_data_cover = Frame(manage_menu_bottom_container)
menu_data_cover.place(relwidth=1, relheight=1)

new_menu_entry_container = Frame(manage_menu_bottom_container)
new_menu_entry_container.place(relwidth=1, relheight=1)
new_menu_data = Frame(new_menu_entry_container)
new_menu_data.pack(anchor=N)
new_menu_header = Label(new_menu_data, text="Please enter menu item details below:", font=("Helvetica 10 bold"), pady=15)
new_menu_header.grid(row=0, column=0, columnspan=2)
item_name_label = Label(new_menu_data, text="Item Name:")
item_name_label.grid(row=1, column=0, padx=20, sticky=E)
item_name_entry = Entry(new_menu_data, width=30)
item_name_entry.grid(row=1, column=1, padx=20, sticky=E)
item_price_label = Label(new_menu_data, text="Item Price:")
item_price_label.grid(row=2, column=0, padx=20, sticky=E)
item_price_entry = Entry(new_menu_data, width=30)
item_price_entry.grid(row=2, column=1, padx=20, sticky=E)
menu_submit_button = Button(new_menu_data, text="Create New Menu Item", width=20, command=confirm_new_menu_clicked)
menu_submit_button.grid(row=3, column=0, pady=25)
menu_cancel_button = Button(new_menu_data, text="Cancel", command=menu_data_cover.lift, width=20)
menu_cancel_button.grid(row=3, column=1, pady=25)
new_menu_entry_container.lower()

edit_menu_container = Frame(manage_menu_bottom_container)
edit_menu_container.place(relwidth=1, relheight=1)
edit_menu_data = Frame(edit_menu_container)
edit_menu_data.pack(anchor=N)
edit_menu_header = Label(edit_menu_data, text="Please enter menu item details below:", font=("Helvetica 10 bold"), pady=15)
edit_menu_header.grid(row=0, column=0, columnspan=2)
eitem_name_label = Label(edit_menu_data, text="Item Name:")
eitem_name_label.grid(row=1, column=0, padx=20, sticky=E)
eitem_name_entry = Entry(edit_menu_data, width=30)
eitem_name_entry.grid(row=1, column=1, padx=20, sticky=E)
eitem_price_label = Label(edit_menu_data, text="Item Price:")
eitem_price_label.grid(row=2, column=0, padx=20, sticky=E)
eitem_price_entry = Entry(edit_menu_data, width=30)
eitem_price_entry.grid(row=2, column=1, padx=20, sticky=E)
emid_label = Label(edit_menu_data, text="Menu Item ID:")
emid_label.grid(row=3, column=0, padx=20, sticky=E)
e_mid = StringVar()
emid_label2 = Label(edit_menu_data, textvariable=e_mid)
emid_label2.grid(row=3, column=1, padx=20, sticky=N)
emenu_submit_button = Button(edit_menu_data, text="Submit Changes", width=20, command=confirm_edit_menu_clicked)
emenu_submit_button.grid(row=4, column=0, pady=15)
emenu_cancel_button = Button(edit_menu_data, text="Cancel", command=menu_data_cover.lift, width=20)
emenu_cancel_button.grid(row=4, column=1, pady=15)
edit_menu_container.lower()

delete_menu_container = Frame(manage_menu_bottom_container)
delete_menu_container.place(relwidth=1, relheight=1)

del_menu_cover = Frame(delete_menu_container)
del_menu_cover.place(relwidth=1, relheight=1)

del_menu_error = Frame(delete_menu_container)
del_menu_error.place(relwidth=1, relheight=1)
del_menu_error_label = Label(del_menu_error, text="ERROR! Can't delete a menu item that is currently linked to a catering event!", font=("Helvetica 12 bold"), pady=40)
del_menu_error_label.pack(anchor=N)
del_menu_error.lower()

del_menu_label_container = Frame(delete_menu_container)
del_menu_label_container.place(relheight=1, relwidth=1)
del_menu_warning = Frame(del_menu_label_container)
del_menu_warning.pack(anchor=N)
del_menu_warning_label = Label(del_menu_warning, text="Are you sure you want to delete this menu item?", font=("Helvetica 12 bold"))
del_menu_warning_label.grid(row=0, column=0, pady=20, columnspan=2)
del_menu_warning_label2 = Label(del_menu_warning, text="WARNING: This action is PERMANENT and cannot be undone!", font=("Helvetica 10"), fg='red')
del_menu_warning_label2.grid(row=1, column=0, columnspan=2, pady=10)
del_menu_confirm_button = Button(del_menu_warning, text="CONFIRM DELETE", command=delete_menu_confirmed)
del_menu_confirm_button.grid(row=2, column=0, padx=20)
del_menu_cancel_button = Button(del_menu_warning, text="Cancel", command=menu_data_cover.lift)
del_menu_cancel_button.grid(row=2, column=1, padx=20)
del_menu_warning.lower()
delete_menu_container.lower()

manage_menu_main_frame.lower()
#end manage menu

#begin create event
create_event_main_frame = Frame(catering_data_container)
create_event_main_frame.place(relwidth=1, relheight=1)
create_event_head_container = Frame(create_event_main_frame, padx=3)
create_event_head_container.place(relwidth=.27, relheight=1)
customer_list_tree_label = Label(create_event_head_container, text="Which customer is\n this event for?", font=("Arial 10 bold"), pady=5)
customer_list_tree_label.pack()
customer_list_tree_container = Frame(create_event_head_container)
customer_list_tree_container.pack(fill=BOTH, expand=YES)

customer_list_tree = ttk.Treeview(customer_list_tree_container)
customer_list_tree.pack(fill=BOTH, expand=YES)
customer_list_tree['show'] = 'headings'
customer_list_tree['columns'] = ('ID', 'Name')
customer_list_tree.column("ID", width=15, anchor=N)
customer_list_tree.column("Name", width=85, anchor=N)
customer_list_tree.heading("ID", text="ID")
customer_list_tree.heading("Name", text="Name")
update_customer_list()

create_event_data_frame = Frame(create_event_main_frame)
create_event_data_frame.place(relheight=1, relwidth=.73, relx=.27)

catering_options_container = Frame(create_event_data_frame)
catering_options_container.place(relheight=.8, relwidth=1)

catering_options_data = Frame(catering_options_container)
catering_options_data.pack(anchor=N)
catering_event_store_label = Label(catering_options_data, text="Select a store:")
catering_event_store_label.grid(row=0, column=0, padx=20, pady=10, sticky=E)
event_stores_svar = StringVar()
event_stores_svar.set("")
catering_store_cb = ttk.Combobox(catering_options_data, textvariable=event_stores_svar, values=all_stores, state='readonly', width=30)
catering_store_cb.grid(row=0, column=1, padx=20, pady=10, sticky=W)
event_date_label = Label(catering_options_data, text="Enter the event date (MM/DD/YYYY):")
event_date_label.grid(row=1, column=0, padx=20, pady=5, sticky=E)
event_date_entry = Entry(catering_options_data, width=33)
event_date_entry.grid(row=1, column=1, padx=20, pady=5, stick=W)
event_date_entry.insert(0, "")
begin_event_button = Button(catering_options_data, text="Create Event", padx=15, command=begin_event_clicked)
begin_event_button.grid(row=2, column=0, columnspan=2, pady=10)

catering_menu_container = Frame(catering_options_container)
catering_menu_container.pack(fill=BOTH, expand=YES)

catering_buttons_cover = Frame(create_event_data_frame)
catering_buttons_cover.place(relwidth=1, relheight=.2, rely=.8)
catering_buttons_container = Frame(create_event_data_frame)
catering_buttons_container.place(relwidth=1, relheight=.2, rely=.8)
catering_buttons_data = Frame(catering_buttons_container)
catering_buttons_data.pack(anchor=N, pady=20)
submit_event_button = Button(catering_buttons_data, text="Submit New Event", command=submit_event_clicked, width=25)
submit_event_button.grid(row=0, column=0)
cancel_event_button = Button(catering_buttons_data, text="Cancel Event", command=cancel_event_clicked, width=25)
cancel_event_button.grid(row=0, column=1)
catering_buttons_container.lower()
create_event_main_frame.lower()
#end create event

#begin view events
view_events_main_frame = Frame(catering_data_container)
view_events_main_frame.place(relwidth=1, relheight=1)
view_events_header = PanedWindow(view_events_main_frame)
view_events_header.place(relwidth=1, relheight=.2)
view_events_header_data = Frame(view_events_header)
view_events_header_data.pack(anchor=N)
select_events_header_label = Label(view_events_header_data, text="Please choose from the options below to view existing events", font=('Helvetica 12 bold'))
select_events_header_label.grid(column=0, row=0, columnspan=3, sticky=N)
select_events_store_label = Label(view_events_header_data, text="Select a store ID:")
select_events_store_label.grid(row=1, column=0)
eventsstores_svar = StringVar()
eventsstores_svar.set("All Stores")
events_stores_cb = ttk.Combobox(view_events_header_data, textvariable=eventsstores_svar, values=stores_with_all, state='readonly', width=30)
events_stores_cb.grid(row=2, column=0)
select_cust_sup_label = Label(view_events_header_data, text="Customer's last name:\n(Optional - leave blank to omit from search")
select_cust_sup_label.grid(row=3, column=0)
events_cust_entry = Entry(view_events_header_data, width=30)
events_cust_entry.grid(row=4, column=0)
events_cust_entry.insert(0, "")
event_var = StringVar()
event_var.set('both')
r1_events = Radiobutton(view_events_header_data, text='Past Events', variable=event_var, value='past')
r1_events.grid(row=2, column=1, sticky=W, padx=15)
r2_events = Radiobutton(view_events_header_data, text='Future Events', variable=event_var, value='future')
r2_events.grid(row=3, column=1, sticky=W, padx=15)
r3_events = Radiobutton(view_events_header_data, text='Both', variable=event_var, value='both')
r3_events.grid(row=4, column=1, sticky=W, padx=15)
get_events_button = Button(view_events_header_data, text="SEARCH EVENTS", width=20, command=get_events_clicked)
get_events_button.grid(column=2, row=3, sticky=NSEW, padx=15)

events_bottom_container = Frame(view_events_main_frame)
events_bottom_container.place(relwidth=1, relheight=.8, rely=.2)
events_tree_container= Frame(events_bottom_container)
events_tree_container.place(relwidth=.48, relx=.003, relheight=1)
events_tree = ttk.Treeview(events_tree_container)
events_tree['show'] = 'headings'
events_tree['columns'] = ('Event ID', 'First Name', 'Last Name', 'Store ID', 'Event Date')
events_tree.pack(fill=BOTH, expand=YES)
events_tree.column("Event ID", width=10, anchor='center')
events_tree.column("First Name", width=10, anchor='center')
events_tree.column("Last Name", width=10, anchor='center')
events_tree.column("Store ID", width=10, anchor='center')
events_tree.column("Event Date", width=10, anchor='center')
events_tree.heading("Event ID", text="Event ID")
events_tree.heading("First Name", text="First Name")
events_tree.heading("Last Name", text="Last Name")
events_tree.heading("Store ID", text="Store ID")
events_tree.heading("Event Date", text="Event Date")
events_tree.bind("<<TreeviewSelect>>", event_selected)

events_details_container = Frame(events_bottom_container)
events_details_container.place(relheight=1, relwidth=.48, relx=.518)
event_dets_tree_container = Frame(events_details_container)
event_dets_tree_container.place(relheight=.6, relwidth=1)
event_details_tree = ttk.Treeview(event_dets_tree_container)
event_details_tree['show'] = 'headings'
event_details_tree['columns'] = ('Menu Item', 'Item Price', 'Total Ordered', 'Total Cost')
event_details_tree.pack(fill=BOTH, expand=YES)
event_details_tree.column("Menu Item", width=10, anchor='w')
event_details_tree.column("Item Price", width=10, anchor='center')
event_details_tree.column("Total Ordered", width=10, anchor='center')
event_details_tree.column("Total Cost", width=10, anchor='center')
event_details_tree.heading("Menu Item", text="Menu Item")
event_details_tree.heading("Item Price", text="Item Price")
event_details_tree.heading("Total Ordered", text="Total Ordered")
event_details_tree.heading("Total Cost", text="Total Cost")

cust_details_container = Frame(events_details_container, bg='white', highlightthickness=.5, highlightbackground='grey')
cust_details_container.place(relwidth=1, relheight=.38, rely=.61)
cust_details_data = Frame(cust_details_container, bg='white')
cust_details_data.pack(anchor=N)
cust_details_header = Label(cust_details_data, bg='white', text="CUSTOMER CONTACT DETAILS", font=("Arial 10 bold"))
cust_details_header.grid(row=0, column=0, columnspan=2, pady=10)
cust_id_label = Label(cust_details_data, bg='white', text="Customer ID:")
cust_id_label.grid(row=1, column=0, pady=10, sticky=W)
cid_svar = StringVar()
cust_id_data = Label(cust_details_data, bg='white', textvariable=cid_svar)
cust_id_data.grid(row=1, column=1, pady=10, sticky=W)
cust_name_label = Label(cust_details_data, bg='white', text="Customer Name:")
cust_name_label.grid(row=2, column=0, pady=10, sticky=W)
cn_svar = StringVar()
cust_name_data = Label(cust_details_data, bg='white', textvariable=cn_svar)
cust_name_data.grid(row=2, column=1, pady=10, sticky=W)
cust_phone_label = Label(cust_details_data, text="Customer Phone:", bg='white')
cust_phone_label.grid(row=3, column=0, sticky=W)
cp_svar = StringVar()
cust_phone_data = Label(cust_details_data, bg='white', textvariable=cp_svar)
cust_phone_data.grid(row=3, column=1, pady=10, sticky=W)
cust_email_label = Label(cust_details_data, text="Customer Email:", bg='white')
cust_email_label.grid(row=4, column=0, sticky=W)
ce_svar = StringVar()
cust_email_data = Label(cust_details_data, bg='white', textvariable=ce_svar)
cust_email_data.grid(row=4, column=1, pady=10, sticky=W)

view_events_main_frame.lower()
# end view events

#begin cancel event
delete_event_main_frame = Frame(catering_data_container)
delete_event_main_frame.place(relwidth=1, relheight=1)
delete_event_header = Frame(delete_event_main_frame)
delete_event_header.place(relwidth=1, relheight=.2)
delete_event_header_data = Frame(delete_event_header)
delete_event_header_data.pack(anchor=N)
delete_event_header_label = Label(delete_event_header_data, text="Select event details below.", font=("Helvetica 12 bold"))
delete_event_header_label.grid(row=0, column=0, columnspan=4)
delete_event_header_label2 = Label(delete_event_header_data, text="(Please note: you can only cancel or delete events that have no recorded payments)", font=("Helvetica 10"))
delete_event_header_label2.grid(row=1, column=0, columnspan=4, pady=10)
delete_event_store_label = Label(delete_event_header_data, text="Select a Store ID:")
delete_event_store_label.grid(row=2, column=0, padx=10)
delete_event_store_cb = ttk.Combobox(delete_event_header_data, textvariable=orderstores_svar, values=stores_with_all, state='readonly', width=30)
delete_event_store_cb.grid(row=2, column=1, padx=10)
delete_event_view_button = Button(delete_event_header_data, text="VIEW EVENTS", command=delete_event_view_orders)
delete_event_view_button.grid(row=3, column=0, columnspan=4, pady=10)

delete_event_tree_container = Frame(delete_event_main_frame)
delete_event_tree_container.place(relheight=.5, relwidth=1, rely=.2)
delete_event_tree = ttk.Treeview(delete_event_tree_container)
delete_event_tree.pack(fill=BOTH, expand=YES)
delete_event_tree['show'] = 'headings'
delete_event_tree['columns'] = ('Event ID', 'Store ID', 'Customer', 'Event Date', 'Amount Due', 'Amount Paid')
delete_event_tree.column("Event ID", width=5)
delete_event_tree.column("Store ID", width=5)
delete_event_tree.column("Customer", width=10)
delete_event_tree.column("Event Date", width=10)
delete_event_tree.column("Amount Due", width=10)
delete_event_tree.column("Amount Paid", width=10)

delete_event_tree.heading("Event ID", text="Event ID")
delete_event_tree.heading("Store ID", text="Store ID")
delete_event_tree.heading("Customer", text="Customer")
delete_event_tree.heading("Event Date", text="Event Date")
delete_event_tree.heading("Amount Due", text="Amount Due")
delete_event_tree.heading("Amount Paid", text="Amound Paid")
delete_event_tree.bind("<<TreeviewSelect>>", del_event_tree_selected)

delete_event_bottom_container = Frame(delete_event_main_frame)
delete_event_bottom_container.place(relwidth=1, relheight=.3, rely=.7)
delete_event_button_container = Frame(delete_event_bottom_container)
delete_event_button_container.pack(anchor=N)
mark_event_canceled_button = Button(delete_event_button_container, text="Mark Selected Event as Canceled", command=mark_event_as_canceled_clicked, state=DISABLED)
mark_event_canceled_button.grid(row=0, column=0, pady=20, padx=10)
delete_event_button = Button(delete_event_button_container, text="DELETE SELECTED EVENT", command=delete_event_clicked, state=DISABLED)
delete_event_button.grid(row=0, column=1, pady=20)

event_warning_message_cover = Frame(delete_event_bottom_container)
event_warning_message_cover.place(relwidth=1, relheight=.7, rely=.3)
event_warning_message_cancel = Frame(delete_event_bottom_container)
event_warning_message_cancel.place(relwidth=1, relheight=.7, rely=.3)
event_cancel_message = Label(event_warning_message_cancel, text="Are you sure you want to mark this event as canceled? This action cannot be undone.", font=("Arial 11 bold"))
event_cancel_message.pack(anchor=N, pady=15)
event_cancel_confirm_button = Button(event_warning_message_cancel, text="CONFIM", command=event_mark_cancel_cofirmed, width=15)
event_cancel_confirm_button.pack(anchor=CENTER, pady=5)
event_cancel_cancel_button = Button(event_warning_message_cancel, text="CANCEL", command=event_warning_message_cover.lift, width=15)
event_cancel_cancel_button.pack(anchor=CENTER, pady=5)
event_warning_message_cancel.lower()

event_warning_message_del = Frame(delete_event_bottom_container)
event_warning_message_del.place(relwidth=1, relheight=.7, rely=.3)
event_cancel_message = Label(event_warning_message_del, text="Are you sure you want to completely remove this event from your system?\nThis action cannot be undone", font=("Arial 11 bold"))
event_cancel_message.pack(anchor=N, pady=15)
event_cancel_confirm_button = Button(event_warning_message_del, text="CONFIM", command=event_mark_del_cofirmed, width=15)
event_cancel_confirm_button.pack(anchor=CENTER, pady=5)
event_cancel_cancel_button = Button(warning_message_del, text="CANCEL", command=event_warning_message_cover.lift, width=15)
event_cancel_cancel_button.pack(anchor=CENTER, pady=5)
event_warning_message_del.lower()

delete_event_main_frame.lower()
#end cancel event

#begin view invoices
cust_invoices_main_frame = Frame(catering_data_container)
cust_invoices_main_frame.place(relwidth=1, relheight=1)
cust_invoices_header = PanedWindow(cust_invoices_main_frame)
cust_invoices_header.place(relwidth=1, relheight=.18)
cust_invoices_header_data = Frame(cust_invoices_header)
cust_invoices_header_data.pack(anchor=N)
cust_invoices_header_label = Label(cust_invoices_header_data, text="Please choose from the options below to view existing customer invoices", font=('Helvetica 12 bold'))
cust_invoices_header_label.grid(column=0, row=0, columnspan=3, sticky=N)
cust_inv_select_orders_store_label = Label(cust_invoices_header_data, text="Select a store ID:")
cust_inv_select_orders_store_label.grid(row=1, column=0)
cust_inv_stores_cb = ttk.Combobox(cust_invoices_header_data, textvariable=orderstores_svar, values=stores_with_all, state='readonly', width=30)
cust_inv_stores_cb.grid(row=2, column=0)
cust_inv_var = StringVar()
cust_inv_var.set('both')
cust_inv_r1 = Radiobutton(cust_invoices_header_data, text='Balance Outstanding', variable=cust_inv_var, value='outstanding')
cust_inv_r1.grid(row=1, column=1, sticky=W, padx=15)
cust_inv_r2 = Radiobutton(cust_invoices_header_data, text='Balance Paid', variable=cust_inv_var, value='paid')
cust_inv_r2.grid(row=2, column=1, sticky=W, padx=15)
cust_inv_r3 = Radiobutton(cust_invoices_header_data, text='Both', variable=cust_inv_var, value='both')
cust_inv_r3.grid(row=3, column=1, sticky=W, padx=15)
cust_get_invoices_button = Button(cust_invoices_header_data, text="GET INVOICES", width=20, command=get_cust_invoices_clicked)
cust_get_invoices_button.grid(column=2, row=2, sticky=NSEW, padx=15)

cust_invoices_data_frame = Frame(cust_invoices_main_frame)
cust_invoices_data_frame.place(relwidth=1, relheight=.82, rely=.18)
cust_invoices_tree_frame = Frame(cust_invoices_data_frame)
cust_invoices_tree_frame.place(relwidth=.6, relheight=1, relx=.01)

cust_invoices_tree = ttk.Treeview(cust_invoices_tree_frame)
cust_invoices_tree['show'] = 'headings'
cust_invoices_tree['columns'] = ('Event ID', 'Store ID', 'Customer', 'Event Date', 'Total Due', 'Amount Paid')
cust_invoices_tree.pack(fill=BOTH, expand=YES)
cust_invoices_tree.column("Event ID", width=10, anchor='center')
cust_invoices_tree.column("Store ID", width=10, anchor='center')
cust_invoices_tree.column("Customer", width=10, anchor='center')
cust_invoices_tree.column("Event Date", width=10, anchor='center')
cust_invoices_tree.column("Total Due", width=10, anchor='center')
cust_invoices_tree.column("Amount Paid", width=10, anchor='center')
cust_invoices_tree.heading("Event ID", text="Event ID")
cust_invoices_tree.heading("Store ID", text="Store ID")
cust_invoices_tree.heading("Customer", text="Customer")
cust_invoices_tree.heading("Event Date", text="Event Date")
cust_invoices_tree.heading("Total Due", text="Total Due")
cust_invoices_tree.heading("Amount Paid", text="Amount Paid")
cust_invoices_tree.bind("<<TreeviewSelect>>", cust_invoice_selected)

cust_invoices_side_data_container = Frame(cust_invoices_data_frame)
cust_invoices_side_data_container.place(relwidth=.38, relheight=1, relx=.62)
cust_invoices_buttons_container = Frame(cust_invoices_side_data_container)
cust_invoices_buttons_container.place(relwidth=1, relheight=.1)
cust_invoices_buttons = Frame(cust_invoices_buttons_container)
cust_invoices_buttons.pack(anchor=N)
cust_inv_details_button = Button(cust_invoices_buttons, text="View Details for\n Selected Invoice", command=cust_inv_details_clicked, state=DISABLED)
cust_inv_details_button.grid(row=0, column=0, padx=15)
cust_inv_pmt_button = Button(cust_invoices_buttons, text="Log Payment for\n Select Invoice", command=cust_inv_payment_clicked, state=DISABLED)
cust_inv_pmt_button.grid(row=0, column=1, padx=15)

cust_inv_data_cover = Frame(cust_invoices_side_data_container)
cust_inv_data_cover.place(relwidth=1, relheight=.9, rely=.1)
cust_inv_details_frame = Frame(cust_invoices_side_data_container)
cust_inv_details_frame.place(relwidth=1, relheight=.9, rely=.1)
cust_inv_details_label = Label(cust_inv_details_frame, text="Invoice Details", font=("Helvetica 12 bold"))
cust_inv_details_label.grid(row=0, column=0, columnspan=2)
cust_inv_details_cid = Label(cust_inv_details_frame, text="Customer ID:")
cust_inv_details_cid.grid(row=1, column=0, sticky=W)
cust_inv_name = StringVar()
cust_inv_name.set("")
cust_inv_details_name_data = Label(cust_inv_details_frame, textvariable=cust_inv_name)
cust_inv_details_name_data.grid(row=1, column=1, padx=10, sticky=W)
cust_inv_details_phone = Label(cust_inv_details_frame, text="Phone Number:")
cust_inv_details_phone.grid(row=2, column=0, sticky=W)
cust_inv_phone = StringVar()
cust_inv_phone.set("")
cust_inv_phone_data = Label(cust_inv_details_frame, textvariable=cust_inv_phone)
cust_inv_phone_data.grid(row=2, column=1, sticky=W, padx=10)
cust_inv_details_email = Label(cust_inv_details_frame, text="Email:")
cust_inv_details_email.grid(row=3, column=0, sticky=W)
cust_inv_email = StringVar()
cust_inv_email.set("")
cust_inv_details_email_data = Label(cust_inv_details_frame, textvariable=cust_inv_email)
cust_inv_details_email_data.grid(row=3, column=1, sticky=W, padx=10)
cust_inv_details_date = Label(cust_inv_details_frame, text="Event Date:")
cust_inv_details_date.grid(row=4, column=0, sticky=W)
cust_inv_date = StringVar()
cust_inv_date.set("")
cust_inv_details_date_data = Label(cust_inv_details_frame, textvariable=cust_inv_date)
cust_inv_details_date_data.grid(row=4, column=1, sticky=W, padx=10)
cust_payment_details_header = Label(cust_inv_details_frame, text="Payment Details", pady=15, font=("Helvetica 12 bold"))
cust_payment_details_header.grid(row=5, column=0, columnspan=2)
cust_payment_details_id = Label(cust_inv_details_frame, text="Payment ID:")
cust_payment_details_id.grid(row=6, column=0, sticky=W)
cust_payment_id = StringVar()
cust_payment_id.set("N/A")
cust_payment_details_id_data = Label(cust_inv_details_frame, textvariable=cust_payment_id)
cust_payment_details_id_data.grid(row=6, column=1, sticky=W, padx=10)
cust_payment_amount = Label(cust_inv_details_frame, text="Payment Amount:")
cust_payment_amount.grid(row=7, column=0, sticky=W)
cust_pmt_amount = StringVar()
cust_pmt_amount.set("N/A")
cust_payment_amount_data = Label(cust_inv_details_frame, textvariable=cust_pmt_amount)
cust_payment_amount_data.grid(row=7, column=1, sticky=W, padx=10)
cust_payment_date = Label(cust_inv_details_frame, text="Payment Date:")
cust_payment_date.grid(row=8, column=0, sticky=W)
cust_pmt_date = StringVar()
cust_pmt_date.set("N/A")
cust_payment_date_data = Label(cust_inv_details_frame, textvariable=cust_pmt_date)
cust_payment_date_data.grid(row=8, column=1, sticky=W, padx=10)
cust_inv_details_frame.lower()

cust_log_pmt_frame = Frame(cust_invoices_side_data_container)
cust_log_pmt_frame.place(relwidth=1, relheight=.9, rely=.1)
cust_log_pmt_frame_cover = Frame(cust_invoices_side_data_container)
cust_log_pmt_frame_cover.place(relwidth=1, relheight=.9, rely=.1)

cust_log_pmt_paid = Frame(cust_log_pmt_frame)
cust_log_pmt_paid.place(relwidth=1, relheight=1)
cust_already_paid_label = Label(cust_log_pmt_paid, text="This invoice has already been paid!", font="Helvetica 12 bold")
cust_already_paid_label.grid(row=0, column=0)
cust_log_pmt_frame.lower()

cust_log_pmt_details = Frame(cust_log_pmt_frame)
cust_log_pmt_details.place(relwidth=1, relheight=1)
cust_date_paid_label = Label(cust_log_pmt_details, text="Enter the payment date:")
cust_date_paid_label.grid(row=0, column=0, pady=15)
cust_date_paid_entry = Entry(cust_log_pmt_details)
cust_date_paid_entry.grid(row=0, column=1, pady=15)
cust_submit_payment_button = Button(cust_log_pmt_details, text="Submit Payment", command=cust_submit_pmt_clicked)
cust_submit_payment_button.grid(row=1, column=0, pady=15)
cust_cancel_payment_button = Button(cust_log_pmt_details, text="Cancel Payment", command=cust_log_pmt_details.lower)
cust_cancel_payment_button.grid(row=1, column=1, pady=15)
cust_log_pmt_details.lower()

cust_log_pmt_frame.lower()
cust_invoices_main_frame.lower()
#end view invoices



#END CATERING TAB

#BEGIN REPORTS TAB
admin_notebook.add(admin_reports_frame, text="Reports")
reports_buttons_container = Frame(admin_reports_frame, bg='grey')
reports_buttons_container.pack(side=LEFT, fill=Y)
inventory_reports_label = Label(reports_buttons_container, text="INVENTORY REPORTS", font=('Helvetica 12 bold'), bg='white', highlightthickness=.5, highlightbackground='grey')
inventory_reports_label.pack(pady=10, fill=X)
items_to_be_ordered_report = Button(reports_buttons_container, text="Items To Order", command=items_to_order_reports)
items_to_be_ordered_report.pack(pady=10, fill=X)
items_incorrectly_ordered_report = Button(reports_buttons_container, text="Items Incorrectly Ordered", command=items_incorrectly_ordered_reports)
items_incorrectly_ordered_report.pack(pady=10, fill=X)
misc_reports_label = Label(reports_buttons_container, text="MISC. REPORTS", font=('Helvetica 12 bold'), bg='white', highlightthickness=.5, highlightbackground='grey')
misc_reports_label.pack(pady=10, fill=X)
canceled_orders_report = Button(reports_buttons_container, text="View Canceled Orders", command=canceled_orders_reports)
canceled_orders_report.pack(pady=10, fill=X)
canceled_events_report = Button(reports_buttons_container, text="View Canceled Events", command=canceled_event_reports)
canceled_events_report.pack(pady=10, fill=X)



reports_data_container = Frame(admin_reports_frame)
reports_data_container.pack(fill=BOTH, expand=True, padx=5)

reports_main_frame = Frame(reports_data_container)
reports_main_frame.place(relwidth=1, relheight=1)
reports_frame_message = Label(reports_main_frame, text="Please select an option from the left", font=('Helvetica 20 bold'))
reports_frame_message.place(relx=.25, rely=.3)

#begin items to order 
items_to_order_frame = Frame(reports_data_container)
items_to_order_frame.place(relheight=1, relwidth=1)
items_to_order_header = Frame(items_to_order_frame)
items_to_order_header.place(relheight=.3, relwidth=1)
items_to_order_label = Label(items_to_order_header, text="Choose a store and product catergory below to see a report\n of items that should be placed on the next order.", font=("Helvetica 12 bold"))
items_to_order_label.pack(anchor=N, pady=10)
items_to_order_store_label = Label(items_to_order_header, text="Select a store", font=("Helvetica 10 bold"))
items_to_order_store_label.pack(anchor=N, pady=5)
items_to_order_store_cb = ttk.Combobox(items_to_order_header, values=all_stores, state='readonly')
items_to_order_store_cb.pack(fill=X)
items_to_order_prod_label = Label(items_to_order_header, text="Select a product tye", font=("Helvetica 10 bold"))
items_to_order_prod_label.pack(anchor=N, pady=5)
items_to_order_prod_cb = ttk.Combobox(items_to_order_header, values=options, state='readonly')
items_to_order_prod_cb.pack(fill=X)
items_to_order_get_report = Button(items_to_order_header, text="VIEW REPORT", command=get_items_to_order_report, width=30, font=('Helvetica 10'))
items_to_order_get_report.pack(anchor=N, pady=10)

items_to_order_bottom_container = Frame(items_to_order_frame)
items_to_order_bottom_container.place(relwidth=1, relheight=.7, rely=.3)
items_to_order_tree_container = Frame(items_to_order_bottom_container)
items_to_order_tree_container.place(relheight=1, relwidth=1)

items_to_order_tree = ttk.Treeview(items_to_order_tree_container)
items_to_order_tree.pack(fill=BOTH, expand=YES)
items_to_order_tree['show'] = 'headings'
items_to_order_tree['columns'] = ('Store ID', 'Supplier', 'Item Name', 'Current Case Qty', 'Par Case Qty', 'Cases to Order')
items_to_order_tree.column("Store ID", width=10)
items_to_order_tree.column("Supplier", width=10)
items_to_order_tree.column("Item Name", width=40)
items_to_order_tree.column("Current Case Qty", width=10)
items_to_order_tree.column("Par Case Qty", width=10)
items_to_order_tree.column("Cases to Order", width=10)
items_to_order_tree.heading("Store ID", text="Store ID")
items_to_order_tree.heading("Supplier", text="Supplier")
items_to_order_tree.heading("Item Name", text="Item Name")
items_to_order_tree.heading("Current Case Qty", text="Current Case Qty")
items_to_order_tree.heading("Par Case Qty", text="Par Case Qty")
items_to_order_tree.heading("Cases to Order", text="Cases to Order")
items_to_order_frame.lower()
#end items to order

#begin incorect items
inc_items_frame = Frame(reports_data_container)
inc_items_frame.place(relheight=1, relwidth=1)
inc_items_header = Frame(inc_items_frame)
inc_items_header.place(relheight=.3, relwidth=1)
inc_items_label = Label(inc_items_header, text="Choose a store and product type to view\n a report of items that have been incorrectly ordered", font=("Helvetica 12 bold"))
inc_items_label.pack(anchor=N, pady=10)
inc_items_store_label = Label(inc_items_header, text="Select a store", font=("Helvetica 10 bold"))
inc_items_store_label.pack(anchor=N, pady=5)
inc_items_store_cb = ttk.Combobox(inc_items_header, values=all_stores, state='readonly')
inc_items_store_cb.pack(fill=X)
inc_items_prod_label = Label(inc_items_header, text="Select a product tye", font=("Helvetica 10 bold"))
inc_items_prod_label.pack(anchor=N, pady=5)
inc_items_prod_cb = ttk.Combobox(inc_items_header, values=options, state='readonly')
inc_items_prod_cb.pack(fill=X)
inc_items_get_report = Button(inc_items_header, text="VIEW REPORT", command=get_inc_items_report, width=30, font=('Helvetica 10'))
inc_items_get_report.pack(anchor=N, pady=10)

inc_items_bottom_container = Frame(inc_items_frame)
inc_items_bottom_container.place(relwidth=1, relheight=.7, rely=.3)
inc_items_tree_container = Frame(inc_items_bottom_container)
inc_items_tree_container.place(relheight=1, relwidth=1)

inc_items_tree = ttk.Treeview(inc_items_tree_container)
inc_items_tree.pack(fill=BOTH, expand=YES)
inc_items_tree['show'] = 'headings'
inc_items_tree['columns'] = ('Store ID', 'Order ID', 'Item Name', 'Current Case Qty', 'Cases Ordered', 'Should have ordered')
inc_items_tree.column("Store ID", width=10)
inc_items_tree.column("Order ID", width=10)
inc_items_tree.column("Item Name", width=40)
inc_items_tree.column("Current Case Qty", width=10)
inc_items_tree.column("Cases Ordered", width=10)
inc_items_tree.column("Should have ordered", width=10)
inc_items_tree.heading("Store ID", text="Store ID")
inc_items_tree.heading("Order ID", text="Order ID")
inc_items_tree.heading("Item Name", text="Item Name")
inc_items_tree.heading("Current Case Qty", text="Current Case Qty")
inc_items_tree.heading("Cases Ordered", text="Cases Ordered")
inc_items_tree.heading("Should have ordered", text="Should have ordered")
inc_items_frame.lower()
#end incorrect orders

#being view canceled orders
canceled_orders_frame = Frame(reports_data_container)
canceled_orders_frame.place(relheight=1, relwidth=1)
canceled_orders_header = Frame(canceled_orders_frame)
canceled_orders_header.place(relheight=.3, relwidth=1)
canceled_orders_label = Label(canceled_orders_header, text="Choose a store to view a report of orders that have been canceled", font=("Helvetica 12 bold"))
canceled_orders_label.pack(anchor=N, pady=10)
canceled_orders_store_label = Label(canceled_orders_header, text="Select a store", font=("Helvetica 10 bold"))
canceled_orders_store_label.pack(anchor=N, pady=5)
canceled_orders_store_cb = ttk.Combobox(canceled_orders_header, values=stores_with_all, state='readonly')
canceled_orders_store_cb.pack(fill=X)
canceled_orders_get_report = Button(canceled_orders_header, text="VIEW REPORT", command=view_canceled_orders, width=30, font=('Helvetica 10'))
canceled_orders_get_report.pack(anchor=N, pady=10)

canceled_orders_bottom_container = Frame(canceled_orders_frame)
canceled_orders_bottom_container.place(relwidth=1, relheight=.7, rely=.3)
canceled_orders_tree_container = Frame(canceled_orders_bottom_container)
canceled_orders_tree_container.place(relheight=1, relwidth=1)

canceled_orders_tree = ttk.Treeview(canceled_orders_tree_container)
canceled_orders_tree.pack(fill=BOTH, expand=YES)
canceled_orders_tree['show'] = 'headings'
canceled_orders_tree['columns'] = ('Store ID', 'Order ID', 'Supplier Name', 'Date Placed', 'Items Ordered', 'Order Cost')
canceled_orders_tree.column("Store ID", width=10, anchor=N)
canceled_orders_tree.column("Order ID", width=10, anchor=N)
canceled_orders_tree.column("Supplier Name", width=40)
canceled_orders_tree.column("Date Placed", width=10)
canceled_orders_tree.column("Items Ordered", width=10, anchor=N)
canceled_orders_tree.column("Order Cost", width=10)
canceled_orders_tree.heading("Store ID", text="Store ID")
canceled_orders_tree.heading("Order ID", text="Order ID")
canceled_orders_tree.heading("Supplier Name", text="Supplier Name")
canceled_orders_tree.heading("Date Placed", text="Date Placed")
canceled_orders_tree.heading("Items Ordered", text="Items Ordered")
canceled_orders_tree.heading("Order Cost", text="Order Cost")
canceled_orders_frame.lower()
#end canceled orders

#begin view canceled events
canceled_events_frame = Frame(reports_data_container)
canceled_events_frame.place(relheight=1, relwidth=1)
canceled_events_header = Frame(canceled_events_frame)
canceled_events_header.place(relheight=.3, relwidth=1)
canceled_events_label = Label(canceled_events_header, text="Choose a store to view a report of events that have been canceled", font=("Helvetica 12 bold"))
canceled_events_label.pack(anchor=N, pady=10)
canceled_events_store_label = Label(canceled_events_header, text="Select a store", font=("Helvetica 10 bold"))
canceled_events_store_label.pack(anchor=N, pady=5)
canceled_events_store_cb = ttk.Combobox(canceled_events_header, values=stores_with_all, state='readonly')
canceled_events_store_cb.pack(fill=X)
canceled_events_get_report = Button(canceled_events_header, text="VIEW REPORT", command=view_canceled_events, width=30, font=('Helvetica 10'))
canceled_events_get_report.pack(anchor=N, pady=10)

canceled_events_bottom_container = Frame(canceled_events_frame)
canceled_events_bottom_container.place(relwidth=1, relheight=.7, rely=.3)
canceled_events_tree_container = Frame(canceled_events_bottom_container)
canceled_events_tree_container.place(relheight=1, relwidth=1)

canceled_events_tree = ttk.Treeview(canceled_events_tree_container)
canceled_events_tree.pack(fill=BOTH, expand=YES)
canceled_events_tree['show'] = 'headings'
canceled_events_tree['columns'] = ('Store ID', 'Event ID', 'Customer Name', 'Event Date', 'Event Cost')
canceled_events_tree.column("Store ID", width=10, anchor=N)
canceled_events_tree.column("Event ID", width=10, anchor=N)
canceled_events_tree.column("Customer Name", width=40)
canceled_events_tree.column("Event Date", width=10)
canceled_events_tree.column("Event Cost", width=10)
canceled_events_tree.heading("Store ID", text="Store ID")
canceled_events_tree.heading("Event ID", text="Event ID")
canceled_events_tree.heading("Customer Name", text="Customer Name")
canceled_events_tree.heading("Event Date", text="Event Date")
canceled_events_tree.heading("Event Cost", text="Event Cost")
canceled_events_frame.lower()
#end canceled events

#END REPORTS TAB

##END ADMIN NOTEBOOK##


#This frame is brought to the front after a successful user login
user_logged_in = Frame(root, bg='#454040', highlightbackground="#332e2d", highlightthickness=1)
user_logged_in.place(relx=.5, rely=.5, anchor='c', width=968, height=738)

##BEGIN USER NOTEBOOK##
#Using a notebook for simplified navigation
user_notebook = ttk.Notebook(user_logged_in)
user_notebook.pack(fill="both", expand=True)


#Creating a frame for each tab of the notebook
user_main_frame = Frame(user_notebook, width=968, height=738)

#BEGIN WELCOME TAB
user_notebook.add(user_main_frame, text="Welcome Page")
un_user_text = StringVar()
welcome_un = Label(user_main_frame, textvariable=un_user_text)
welcome_un.pack(anchor="center", pady=20)
welcome_label = Label(user_main_frame, text=f"You are logged in to the Blockhouse Inventory Management System.\n Use the tabs above to see all available options.")
welcome_label.pack(anchor="center", pady=25)
logout_button = Button(user_main_frame, text="Logout", command=logout_clicked)
logout_button.pack(anchor="center")
#END WELCOME TAB

##END USERS NOTEBOOK##

#Lowering the admin/user page so that it is invisible until a successful login occurs
admin_logged_in.lower()
user_logged_in.lower()

root.mainloop()


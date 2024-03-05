class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, name, new_phone_number):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = new_phone_number
                print(f"Contact {name} updated successfully.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")

# Sample usage:
if __name__ == "__main__":
    contact_manager = ContactManager()

    # Adding contacts
    contact_manager.add_contact(Contact("John Doe", "1234567890", "john@example.com", "123 Main St"))
    contact_manager.add_contact(Contact("Jane Smith", "9876543210", "jane@example.com", "456 Elm St"))

    # Viewing contacts
    print("All Contacts:")
    contact_manager.view_contacts()

    # Searching contacts
    keyword = input("Enter name or phone number to search: ")
    found_contacts = contact_manager.search_contact(keyword)
    if found_contacts:
        print("Found Contacts:")
        for contact in found_contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")
    else:
        print("No contacts found.")

    # Updating contact
    contact_manager.update_contact("John Doe", "5555555555")

    # Deleting contact
    contact_manager.delete_contact("Jane Smith")

    # Viewing contacts after updates
    print("All Contacts after updates:")
    contact_manager.view_contacts()

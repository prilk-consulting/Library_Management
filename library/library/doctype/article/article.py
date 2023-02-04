# Copyright (c) 2023, Sandeep Sabat and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class Article(WebsiteGenerator):
	def before_save(self):
		self.route = self.name
		self.is_published = True

# lib@gmai.com
# Library@123
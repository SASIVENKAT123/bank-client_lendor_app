from ._anvil_designer import tdTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class td(tdTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.avlbal")

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vblr")

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.ld")

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vlo")

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vep")

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vcl")

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vler")

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vlfr")

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.rta")

  def link_10_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vdp")

  def link_11_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.opbal")

  def link_12_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vsn")

  def link_13_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.cp")

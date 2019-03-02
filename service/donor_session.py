from django.conf import settings

class ActiveDonor():
	def __init__(self, request):
		self.session = request.session
		active_donor = self.session.get(settings.ACTIVE_DONOR_SESSION_ID)
		if not active_donor:
			active_donor = self.session[settings.ACTIVE_DONOR_SESSION_ID] = {}
		self.active_donor = active_donor

	def add_donation(self, drug_detail):
		"""drug_detail is tuple of drug and its category object"""
		if not self.active_donor.keys()
			self.active_donor['donation_list'] = []
		if drug_detail:
			self.active_donor['donation_list'].append(drug_detail)

	def add_supply_detail(self, supply_detail):
		self.active_donor['supply_detail'] = supply_detail

	def save(self):
		self.session.modified = True

	def clear(self):
		del self.session[settings.ACTIVE_DONOR_SESSION_ID]
        self.save()








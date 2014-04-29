import foxpath
from foxpath import test
#f="dfid-tz.xml"
f='dfid-tz.xml'
#t='at least one (sector[@vocabulary="DAC"]/@code or sector[not(@vocabulary)]/@code) is on list Sector?'
#t='at least one country-budget-items[@vocabulary="1"]/budget-item/@code is on list BudgetIdentifier?'
#t="default-aid-type/@code or transaction/aid-type/@code is on list AidType (if activity-status/@code is at least 2)?"
lists={'Sector': ['13040'], 
       'BudgetIdentifier': ['5.1.1'], 
       'AidType': ['A01'],
       'CollaborationType': ['1'],
       'ActivityStatus': ['2'],
       'FinanceType': ['1'],
       'FlowType': ['10'],
       'TiedStatus': ['3'],
      }

list_tests = ['default-aid-type/@code or transaction/aid-type/@code is on list AidType (if activity-status/@code is at least 2)?',
         'at least one country-budget-items[@vocabulary="1"]/budget-item/@code is on list BudgetIdentifier (if activity-status/@code is at least 2 and (default-aid-type/@code or transaction/aid-type/@code is not A01 or A02))?',
         'collaboration-type/@code is on list CollaborationType (if activity-status/@code is at least 2)?',
         'activity-status/@code is on list ActivityStatus?',
         'default-finance-type/@code or transaction/finance-type/@code is on list FinanceType (if activity-status/@code is at least 2)?',
         'default-flow-type/@code or transaction/flow-type/@code is on list FlowType (if activity-status/@code is at least 2)?',
         'at least one (sector[@vocabulary="DAC"]/@code or sector[not(@vocabulary)]/@code) is on list Sector?',
         'default-tied-status/@code or transaction/tied-status/@code is on list TiedStatus (if activity-status/@code is at least 2)?',
        ]

nonlist_tests = [ 
        "default-aid-type or transaction/aid-type exists (if activity-status/@code is at least 2)?",
        "document-link/category[@code='B04'] exists?",
        "document-link/category[@code='B01'] exists?",
        "document-link/category[@code='B06'] exists?",
        "document-link/category[@code='A05'] exists (if activity-status/@code is at least 2 and (default-aid-type/@code or transaction/aid-type/@code is not A01))?",
        "capital-spend exists (if activity-status/@code is at least 2 and (default-aid-type/@code or transaction/aid-type/@code is not A01 or A02))?",
        "collaboration-type exists (if activity-status/@code is at least 2)?",
        "conditions or document-link/category[@code='A04'] exists (if activity-status/@code is at least 2 and conditions/@attached is not 0)?",
        "contact-info exists?",
        "document-link/category[@code='A06'] or document-link/category[@code='A11'] exists (if activity-status/@code is at least 2 and (default-aid-type/@code or transaction/aid-type/@code is not A01))?",
        "budget or planned-disbursement is available forward (if activity-status/@code is at least 2)?",
        "budget or planned-disbursement is available forward by quarters (if activity-status/@code is at least 2)?",
        "document-link/category[@code='B03'] exists?",
        "activity-status exists?",
        "activity-date[@type='end-actual'] exists (if activity-status/@code is at least 3)?",
        "activity-date[@type='start-actual'] exists (if activity-status/@code is at least 2)?",
        "activity-date[@type='end-planned'] exists?",
        "activity-date[@type='start-planned'] exists?",
        "description/text() exists?",
        "description/text() has more than 40 characters?",
        "document-link/category[@code='A07'] exists (if activity-status/@code is at least 3)?",
        "transaction/transaction-type[@code='D'] or transaction/transaction-type[@code='E'] exists (if activity-status/@code is at least 2)?",
        "transaction/transaction-type[@code='C'] exists (if activity-status/@code is at least 2)?",
        "default-finance-type or transaction/finance-type exists (if activity-status/@code is at least 2)?",
        "default-flow-type or transaction/flow-type exists (if activity-status/@code is at least 2)?",
        "document-link/category[@code='A01'] exists (if activity-status/@code is at least 2)?",
        "participating-org[@role='Implementing'] exists (if activity-status/@code is at least 2)?",
        "location exists (if activity-status/@code is at least 2 and recipient-region/@code is not 998)?",
        "location/coordinates exists (if activity-status/@code is at least 2 and recipient-region/@code is not 998)?",
        "document-link/category[@code='A09'] exists (if activity-status/@code is at least 2 and (default-aid-type/@code or transaction/aid-type/@code is not C01))?",
        "document-link/category[@code='A02'] or description[@type='2'] exists (if activity-status/@code is at least 2)?",
        "document-link/category[@code='B05'] exists?",
        "document-link/category[@code='A08'] or result exists (if activity-status/@code is at least 2)?",
        "sector exists?",
        "document-link/category[@code='B02'] exists?",
        "document-link/category[@code='A10'] exists (if activity-status/@code is at least 2 and (default-aid-type/@code or transaction/aid-type/@code is not A01))?",
        "default-tied-status or transaction/tied-status exists (if activity-status/@code is at least 2)?",
        "title/text() exists?",
        "title/text() has more than 10 characters?",
        "iati-identifier exists?",
        "iati-identifier/text() starts with reporting-org/@ref?",
        "activity-date[@type='end-planned']/@iso-date or activity-date[@type='end-planned']/text() or activity-date[@type='end-actual']/@iso-date or activity-date[@type='end-actual']/text() or transaction-date/@iso-date (for any transaction[transaction-type/@code='D']|transaction[transaction-type/@code='E']) is less than 13 months ago?",
]

def check_list_test(f, t, lists):
    test.test_doc_lists(f,t,lists)

def check_nonlist_test(f, t):
    test.test_doc(f,t)

for t in list_tests:
    check_list_test(f, t, lists)

for t in nonlist_tests:
    check_nonlist_test(f,t)
##################################################
# file: SharingService_client.py
#
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     D:\workspace\digsby\Digsby.py --no-traceback-dialog --multi --server=api5.digsby.org
#
##################################################

from SharingService_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI

import util.callbacks as callbacks
import util.network.soap as soap

import ZSI.wstools.Namespaces as NS
from msn.SOAP import Namespaces as MSNS, MSNBindingSOAP

# Locator
class SharingServiceLocator:
    FindMembershipPort_address = "https://contacts.msn.com/abservice/SharingService.asmx"
    def getFindMembershipPortAddress(self):
        return SharingServiceLocator.FindMembershipPort_address
    def getFindMembershipPort(self, url=None, **kw):
        return SharingServiceBindingSOAP(url or SharingServiceLocator.FindMembershipPort_address, **kw)
    AddMemberPort_address = "https://contacts.msn.com/abservice/SharingService.asmx"
    def getAddMemberPortAddress(self):
        return SharingServiceLocator.AddMemberPort_address
    def getAddMemberPort(self, url=None, **kw):
        return SharingServiceBindingSOAP(url or SharingServiceLocator.AddMemberPort_address, **kw)
    DeleteMemberPort_address = "https://contacts.msn.com/abservice/SharingService.asmx"
    def getDeleteMemberPortAddress(self):
        return SharingServiceLocator.DeleteMemberPort_address
    def getDeleteMemberPort(self, url=None, **kw):
        return SharingServiceBindingSOAP(url or SharingServiceLocator.DeleteMemberPort_address, **kw)
    CreateCirclePort_address = "https://contacts.msn.com/abservice/SharingService.asmx"
    def getCreateCirclePortAddress(self):
        return SharingServiceLocator.CreateCirclePort_address
    def getCreateCirclePort(self, url=None, **kw):
        return SharingServiceBindingSOAP(url or SharingServiceLocator.CreateCirclePort_address, **kw)

# Methods
class SharingServiceBindingSOAP(MSNBindingSOAP):

    # op: FindMembership
    @callbacks.callsback
    def FindMembership(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, FindMembershipMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/FindMembership", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: AddMember
    @callbacks.callsback
    def AddMember(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, AddMemberMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/AddMember", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: DeleteMember
    @callbacks.callsback
    def DeleteMember(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, DeleteMemberMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/DeleteMember", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: CreateCircle
    @callbacks.callsback
    def CreateCircle(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, CreateCircleMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/CreateCircle", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

FindMembershipMessage           = GED(MSNS.MSWS.ADDRESS, "FindMembership").pyclass
FindMembershipResponseMessage   = GED(MSNS.MSWS.ADDRESS, "FindMembershipResponse").pyclass
AddMemberMessage                = GED(MSNS.MSWS.ADDRESS, "AddMember").pyclass
AddMemberResponseMessage        = GED(MSNS.MSWS.ADDRESS, "AddMemberResponse").pyclass
DeleteMemberMessage             = GED(MSNS.MSWS.ADDRESS, "DeleteMember").pyclass
DeleteMemberResponseMessage     = GED(MSNS.MSWS.ADDRESS, "DeleteMemberResponse").pyclass
CreateCircleMessage             = GED(MSNS.MSWS.ADDRESS, "CreateCircle").pyclass
CreateCircleResponseMessage     = GED(MSNS.MSWS.ADDRESS, "CreateCircleResponse").pyclass

# Locator
class ABServiceLocator:
    ABFindAllPort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getABFindAllPortAddress(self):
        return ABServiceLocator.ABFindAllPort_address
    def getABFindAllPort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.ABFindAllPort_address, **kw)
    ABContactAddPort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getABContactAddPortAddress(self):
        return ABServiceLocator.ABContactAddPort_address
    def getABContactAddPort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.ABContactAddPort_address, **kw)
    ABContactDeletePort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getABContactDeletePortAddress(self):
        return ABServiceLocator.ABContactDeletePort_address
    def getABContactDeletePort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.ABContactDeletePort_address, **kw)
    ABGroupContactAddPort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getABGroupContactAddPortAddress(self):
        return ABServiceLocator.ABGroupContactAddPort_address
    def getABGroupContactAddPort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.ABGroupContactAddPort_address, **kw)
    ABGroupAddPort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getABGroupAddPortAddress(self):
        return ABServiceLocator.ABGroupAddPort_address
    def getABGroupAddPort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.ABGroupAddPort_address, **kw)
    ABGroupUpdatePort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getABGroupUpdatePortAddress(self):
        return ABServiceLocator.ABGroupUpdatePort_address
    def getABGroupUpdatePort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.ABGroupUpdatePort_address, **kw)
    ABGroupDeletePort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getABGroupDeletePortAddress(self):
        return ABServiceLocator.ABGroupDeletePort_address
    def getABGroupDeletePort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.ABGroupDeletePort_address, **kw)
    ABGroupContactDeletePort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getABGroupContactDeletePortAddress(self):
        return ABServiceLocator.ABGroupContactDeletePort_address
    def getABGroupContactDeletePort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.ABGroupContactDeletePort_address, **kw)
    ABContactUpdatePort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getABContactUpdatePortAddress(self):
        return ABServiceLocator.ABContactUpdatePort_address
    def getABContactUpdatePort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.ABContactUpdatePort_address, **kw)
    ABAddPort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getABAddPortAddress(self):
        return ABServiceLocator.ABAddPort_address
    def getABAddPort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.ABAddPort_address, **kw)
    UpdateDynamicItemPort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getUpdateDynamicItemPortAddress(self):
        return ABServiceLocator.UpdateDynamicItemPort_address
    def getUpdateDynamicItemPort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.UpdateDynamicItemPort_address, **kw)
    ABFindContactsPagedPort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getABFindContactsPagedPortAddress(self):
        return ABServiceLocator.ABFindContactsPagedPort_address
    def getABFindContactsPagedPort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.ABFindContactsPagedPort_address, **kw)
    CreateContactPort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getCreateContactPortAddress(self):
        return ABServiceLocator.CreateContactPort_address
    def getCreateContactPort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.CreateContactPort_address, **kw)
    ManageWLConnectionPort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getManageWLConnectionPortAddress(self):
        return ABServiceLocator.ManageWLConnectionPort_address
    def getManageWLConnectionPort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.ManageWLConnectionPort_address, **kw)
    BreakConnectionPort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getBreakConnectionPortAddress(self):
        return ABServiceLocator.BreakConnectionPort_address
    def getBreakConnectionPort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.BreakConnectionPort_address, **kw)
    AddDynamicItemPort_address = "https://contacts.msn.com/abservice/abservice.asmx"
    def getAddDynamicItemPortAddress(self):
        return ABServiceLocator.AddDynamicItemPort_address
    def getAddDynamicItemPort(self, url=None, **kw):
        return ABServiceBindingSOAP(url or ABServiceLocator.AddDynamicItemPort_address, **kw)

# Methods
class ABServiceBindingSOAP(MSNBindingSOAP):

    # op: ABFindAll
    @callbacks.callsback
    def ABFindAll(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, ABFindAllMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/ABFindAll", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: ABContactAdd
    @callbacks.callsback
    def ABContactAdd(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, ABContactAddMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/ABContactAdd", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: ABContactDelete
    @callbacks.callsback
    def ABContactDelete(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, ABContactDeleteMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/ABContactDelete", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: ABGroupContactAdd
    @callbacks.callsback
    def ABGroupContactAdd(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, ABGroupContactAddMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/ABGroupContactAdd", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: ABGroupAdd
    @callbacks.callsback
    def ABGroupAdd(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, ABGroupAddMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/ABGroupAdd", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: ABGroupUpdate
    @callbacks.callsback
    def ABGroupUpdate(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, ABGroupUpdateMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/ABGroupUpdate", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: ABGroupDelete
    @callbacks.callsback
    def ABGroupDelete(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, ABGroupDeleteMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/ABGroupDelete", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: ABGroupContactDelete
    @callbacks.callsback
    def ABGroupContactDelete(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, ABGroupContactDeleteMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/ABGroupContactDelete", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: ABContactUpdate
    @callbacks.callsback
    def ABContactUpdate(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, ABContactUpdateMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/ABContactUpdate", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: ABAdd
    @callbacks.callsback
    def ABAdd(self, request, soapheaders=(), **kw):
        if isinstance(request, ABAddMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/ABAdd", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: UpdateDynamicItem
    @callbacks.callsback
    def UpdateDynamicItem(self, request, soapheaders=(), **kw):
        if isinstance(request, UpdateDynamicItemMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/UpdateDynamicItem", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: ABFindContactsPaged
    @callbacks.callsback
    def ABFindContactsPaged(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, ABFindContactsPagedMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/ABFindContactsPaged", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: CreateContact
    @callbacks.callsback
    def CreateContact(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, CreateContactMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/CreateContact", soapheaders=soapheaders,
                         callback = callback,
                         **kw)


    # op: ManageWLConnection
    @callbacks.callsback
    def ManageWLConnection(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, ManageWLConnectionMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/ManageWLConnection", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

    # op: BreakConnection
    @callbacks.callsback
    def BreakConnection(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, BreakConnectionMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/BreakConnection", soapheaders=soapheaders,
                         callback = callback,
                           **kw)

    # op: AddDynamicItem
    @callbacks.callsback
    def AddDynamicItem(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, AddDynamicItemMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/AddDynamicItem", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

ABFindAllMessage                        = GED(MSNS.MSWS.ADDRESS, "ABFindAll").pyclass
ABFindAllResponseMessage                = GED(MSNS.MSWS.ADDRESS, "ABFindAllResponse").pyclass
ABContactAddMessage                     = GED(MSNS.MSWS.ADDRESS, "ABContactAdd").pyclass
ABContactAddResponseMessage             = GED(MSNS.MSWS.ADDRESS, "ABContactAddResponse").pyclass
ABContactDeleteMessage                  = GED(MSNS.MSWS.ADDRESS, "ABContactDelete").pyclass
ABContactDeleteResponseMessage          = GED(MSNS.MSWS.ADDRESS, "ABContactDeleteResponse").pyclass
ABGroupContactAddMessage                = GED(MSNS.MSWS.ADDRESS, "ABGroupContactAdd").pyclass
ABGroupContactAddResponseMessage        = GED(MSNS.MSWS.ADDRESS, "ABGroupContactAddResponse").pyclass
ABGroupAddMessage                       = GED(MSNS.MSWS.ADDRESS, "ABGroupAdd").pyclass
ABGroupAddResponseMessage               = GED(MSNS.MSWS.ADDRESS, "ABGroupAddResponse").pyclass
ABGroupUpdateMessage                    = GED(MSNS.MSWS.ADDRESS, "ABGroupUpdate").pyclass
ABGroupUpdateResponseMessage            = GED(MSNS.MSWS.ADDRESS, "ABGroupUpdateResponse").pyclass
ABGroupDeleteMessage                    = GED(MSNS.MSWS.ADDRESS, "ABGroupDelete").pyclass
ABGroupDeleteResponseMessage            = GED(MSNS.MSWS.ADDRESS, "ABGroupDeleteResponse").pyclass
ABGroupContactDeleteMessage             = GED(MSNS.MSWS.ADDRESS, "ABGroupContactDelete").pyclass
ABGroupContactDeleteResponseMessage     = GED(MSNS.MSWS.ADDRESS, "ABGroupContactDeleteResponse").pyclass
ABContactUpdateMessage                  = GED(MSNS.MSWS.ADDRESS, "ABContactUpdate").pyclass
ABContactUpdateResponseMessage          = GED(MSNS.MSWS.ADDRESS, "ABContactUpdateResponse").pyclass
ABAddMessage                            = GED(MSNS.MSWS.ADDRESS, "ABAdd").pyclass
ABAddResponseMessage                    = GED(MSNS.MSWS.ADDRESS, "ABAddResponse").pyclass
UpdateDynamicItemMessage                = GED(MSNS.MSWS.ADDRESS, "UpdateDynamicItem").pyclass
UpdateDynamicItemResponseMessage        = GED(MSNS.MSWS.ADDRESS, "UpdateDynamicItemResponse").pyclass
ABFindContactsPagedMessage              = GED(MSNS.MSWS.ADDRESS, "ABFindContactsPaged").pyclass
ABFindContactsPagedResponseMessage      = GED(MSNS.MSWS.ADDRESS, "ABFindContactsPagedResponse").pyclass
CreateContactMessage                    = GED(MSNS.MSWS.ADDRESS, "CreateContact").pyclass
CreateContactResponseMessage            = GED(MSNS.MSWS.ADDRESS, "CreateContactResponse").pyclass
ManageWLConnectionMessage               = GED(MSNS.MSWS.ADDRESS, "ManageWLConnection").pyclass
ManageWLConnectionResponseMessage       = GED(MSNS.MSWS.ADDRESS, "ManageWLConnectionResponse").pyclass
BreakConnectionMessage                  = GED(MSNS.MSWS.ADDRESS, "BreakConnection").pyclass
BreakConnectionResponseMessage          = GED(MSNS.MSWS.ADDRESS, "BreakConnectionResponse").pyclass
AddDynamicItemMessage                   = GED(MSNS.MSWS.ADDRESS, "AddDynamicItem").pyclass
AddDynamicItemResponseMessage           = GED(MSNS.MSWS.ADDRESS, "AddDynamicItemResponse").pyclass

# Locator
class WhatsUpServiceLocator:
    GetContactsRecentActivityPort_address = "http://sup.live.com/whatsnew/whatsnewservice.asmx"
    def getGetContactsRecentActivityPortAddress(self):
        return WhatsUpServiceLocator.GetContactsRecentActivityPort_address
    def getGetContactsRecentActivityPort(self, url=None, **kw):
        return WhatsUpServiceBindingSOAP(url or WhatsUpServiceLocator.GetContactsRecentActivityPort_address, **kw)

# Methods
class WhatsUpServiceBindingSOAP(MSNBindingSOAP):

    # op: GetContactsRecentActivity
    @callbacks.callsback
    def GetContactsRecentActivity(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, GetContactsRecentActivityMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/AddressBook/GetContactsRecentActivity", soapheaders=soapheaders,
                         callback = callback,
                         **kw)
        # no output wsaction

GetContactsRecentActivityMessage            = GED(MSNS.MSWS.ADDRESS, "GetContactsRecentActivity").pyclass
GetContactsRecentActivityResponseMessage    = GED(MSNS.MSWS.ADDRESS, "GetContactsRecentActivityResponse").pyclass

import unittest

import responses

from cul_archives_utils.clio_utils import ClioUtils


class TestClioUtils(unittest.TestCase):
    @responses.activate
    def test_get_clio_marc(self):
        bibid = "3460608"
        response_content = b"01822cam a2200433 a 4500001001400000005001700014008004100031009001900072010001700091020001500108035018900123040001800312043001200330050002700342082001600369100003000385245005200415250001200467260003500479300002100514520009500535650004300630651002700673650002800700650002000728655002600748655002700774655003600801655003300837655002000870655003800890655005200928600004900980648002001029776012101049583009901170852004901269876007001318\x1eSCSB-10668345\x1e20200603122715.0\x1e000605s2001    nyu           000 1 eng  \x1e990086388640203941\x1e  \x1fa^^^00043143^\x1e  \x1fa0385498195\x1e  \x1fa(OCoLC)44425402\x1fz(OCoLC)408597201\x1fz(OCoLC)704048512\x1fz(OCoLC)1022703288\x1fz(OCoLC)1064846417\x1fz(OCoLC)1078055151\x1fz(OCoLC)1081067460\x1fz(OCoLC)1081385385\x1fz(OCoLC)1083411720\x1fz(OCoLC)1087048578\x1e  \x1faDLC\x1fcDLC\x1fdDLC\x1e  \x1fan-us-wv\x1e00\x1faPS3573.H4768\x1fbJ64 2001\x1e00\x1fa813/.54\x1f221\x1e1 \x1faWhitehead, Colson,\x1fd1969-\x1e10\x1faJohn Henry Days :\x1fba novel /\x1fcColson Whitehead.\x1e  \x1fa1st ed.\x1e  \x1faNew York :\x1fbDoubleday,\x1fcc2001.\x1e  \x1fa389 p. ;\x1fc25 cm.\x1e  \x1faE-journalist J. Sutter travels to West Virginia for the first John Henry Days celebration.\x1e 0\x1faAfrican American journalists\x1fvFiction.\x1e 0\x1faWest Virginia\x1fvFiction\x1e 0\x1faRace relations\x1fvFiction\x1e 0\x1faRacism\x1fvFiction\x1e 0\x1faPsychological fiction\x1e 0\x1faPsychological fiction.\x1e 7\x1faRace relations\x1fvFiction.\x1f2gsafd\x1e 7\x1faPsychological fiction\x1f2lcgft\x1e 7\x1faLegends.\x1f2gsafd\x1e 7\x1faFiction\x1f2fast\x1f0(OCoLC)fst01423787\x1e 7\x1faPsychological fiction\x1f2fast\x1f0(OCoLC)fst01726481\x1e10\x1faHenry, John\x1fc(Legendary character)\x1fvFiction.\x1e 7\x1fa2000-2099\x1f2fast\x1e08\x1fiOnline version:\x1faWhitehead, Colson, 1969-\x1ftJohn Henry Days.\x1fb1st ed.\x1fdNew York : Doubleday, \xc2\xa92001\x1fw(OCoLC)606556535\x1e1 \x1facommitted to retain\x1fc20181001\x1fdin perpetuity\x1ffReCAP Shared Collection\x1f5HUL\x1f8222061489140003941\x1e0 \x1fcHD\x1fhPS3573.H4768\x1fiJ64 2001\x1f011454631\x1fbscsbhl\x1e  \x1f011454631\x1f3\x1fa17193241\x1fh \x1fjAvailable\x1fkWID\x1fpHXBFJU\x1ft\x1fxShared\x1fzHW\x1flHD\x1e\x1d"
        responses.get(
            f"https://clio.columbia.edu/catalog/{bibid}.marc", body=response_content,
        )
        clio_marc = ClioUtils().get_clio_marc(bibid)
        self.assertTrue(clio_marc, response_content)

    @responses.activate
    def test_check_clio_status(self):
        bibid = "3460608"
        responses.get(f"https://clio.columbia.edu/catalog/{bibid}")
        clio_status = ClioUtils().check_clio_status(bibid)
        self.assertEqual(clio_status, 200)

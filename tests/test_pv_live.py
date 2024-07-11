from pvlive_api import PVLive

pvl = PVLive()


class TestClass:
    def test_gsp_list(self):
        gsps = pvl.gsp_ids
        assert len(gsps) == 318

    def test_pes_list(self):
        pes = pvl.pes_ids
        assert len(pes) == 15

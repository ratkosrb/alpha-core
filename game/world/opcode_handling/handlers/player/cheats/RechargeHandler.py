from network.packet.PacketReader import PacketReader


class RechargeHandler(object):

    @staticmethod
    def handle(world_session, socket, reader: PacketReader) -> int:
        if not world_session.player_mgr.is_gm:
            return 0

        world_session.player_mgr.recharge_power()
        world_session.player_mgr.send_update_self(world_session.player_mgr.generate_proper_update_packet(is_self=True))

        return 0
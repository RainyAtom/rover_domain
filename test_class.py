from run_simulation import main

class TestClass():
    def test_config(self):
        for x in range(10):
            main("config_agents10.yml")
            main("config_agents20.yml")
            main("config_agents30.yml")
            main("config_agents40.yml")
            main("config_agents50.yml")
            main("config_agents60.yml")
            main("config_agents70.yml")
            main("config_agents80.yml")
            main("config_agents90.yml")
            main("config_agents100.yml")

        # for x in range(10):
        #     main("config_con_radius1.yml")
        #     main("config_con_radius2.yml")
        #     main("config_con_radius3.yml")
        #     main("config_con_radius4.yml")
        #     main("config_con_radius5.yml")
        #     main("config_con_radius6.yml")
        #     main("config_con_radius7.yml")
        #     main("config_con_radius8.yml")
        #     main("config_con_radius9.yml")
        #     main("config_con_radius10.yml")
        #
        # for x in range(10):
        #     main("config_coupling1.yml")
        #     main("config_coupling2.yml")
        #     main("config_coupling3.yml")
        #     main("config_coupling4.yml")
        #     main("config_coupling5.yml")
        #     main("config_coupling6.yml")
        #     main("config_coupling7.yml")
        #     main("config_coupling8.yml")
        #     main("config_coupling9.yml")
        #     main("config_coupling10.yml")
        #
        # for x in range(10):
        #     main("config_pois5.yml")
        #     main("config_pois10.yml")
        #     main("config_pois15.yml")
        #     main("config_pois20.yml")
        #     main("config_pois25.yml")
        #     main("config_pois30.yml")
        #     main("config_pois35.yml")
        #     main("config_pois40.yml")
        #     main("config_pois45.yml")
        #     main("config_pois50.yml")
        #
        # for x in range(10):
        #     main("config_ws10.yml")
        #     main("config_ws20.yml")
        #     main("config_ws30.yml")
        #     main("config_ws40.yml")
        #     main("config_ws50.yml")
        #     main("config_ws60.yml")
        #     main("config_ws70.yml")
        #     main("config_ws80.yml")
        #     main("config_ws90.yml")
        #     main("config_ws100.yml")


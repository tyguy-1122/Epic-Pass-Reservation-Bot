from resort import Resort

class Epic_config():
    def __init__(self, email, password, resort_name, passholders, dates):
        self.reservation_url = 'https://www.epicpass.com/plan-your-trip/lift-access/reservations.aspx?reservation=true'
        self.resort_options = {'Afton Alps':Resort.afton_alps,'Alpine Valley':Resort.alpine_valley ,'Attitash Mountain':Resort.attitash_mountain, 'Beaver Creek':Resort.beaver_creek,
        'Boston Mills Brandywine':Resort.boston_mills_brandywine, 'Breckenridge':Resort.breckenridge, 'Crested Butte':Resort.crested_butte, 'Crotched Mountain':Resort.crotched_mountain, 'Heavenly':Resort.heavenly,
        'Hidden Valley':Resort.hidden_valley, 'Hunter':Resort.hunter, 'Jack Frost Big Boulder':Resort.jack_frost_big_boulder, 'Keystone':Resort.keystone, 'Kirkwood':Resort.kirkwood, 'Liberty Mountain':Resort.liberty_mountain,
        'Mad River Mountain':Resort.mad_river_mountain, 'Mount Sunapee':Resort.mount_sunapee, 'Mt. Brighton':Resort.mt_brighton, 'Mt. Snow':Resort.mt_snow, 'Northstar':Resort.northstar, 'Okemo':Resort.okemo,
        'Paoli Peaks':Resort.paoli_peaks, 'Park City':Resort.park_city, 'Roundtop Mountain':Resort.roundtop_mountain, 'Snow Creek':Resort.snow_creek, 'Stevens Pass':Resort.stevens_pass, 'Stowe':Resort.stowe,
        'Vail':Resort.vail, 'Whistler Blackcomb':Resort.whistler_blackcomb, 'Whitetail':Resort.whitetail, 'Wildcat Mountain':Resort.wildcat_mountain, 'Wilmot Mountain':Resort.wilmot_mountain}

        self.account_keys = {
        "email":email,
        "password":password
        }

        self.reservation_keys = {
            "resort_name":self.resort_options[resort_name],
            "names":passholders,
            "dates":dates
        }


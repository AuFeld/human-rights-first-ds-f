def helper(df):
    count = {}
    for set_of_tags in df["tags"]:
        for tag in set_of_tags:
            if tag in count:
                count[tag] += 1
            else:
                count[tag] = 1

    force = {}
    force['1. Officer Presence'] = 0
    force['2. Nonthreatening Commands'] = 0
    force['3. Threatening Commands'] = 0
    force['4. Soft Technique'] = 0
    force['5. Hard Technique'] = 0
    force['6. Blunt Impact'] = 0
    force['7. Chemical'] = 0
    force['8. Conducted Enery Devices'] = 0
    force['9. Lethal'] = 0

    force['2. Nonthreatening Commands'] += count['abuse-of-power']
    force['3. Threatening Commands'] += count['arrest']
    force['6. Blunt Impact'] += count['baton']
    force['6. Blunt Impact'] += count['bean-bag']
    force['5. Hard Technique'] += count['beat']
    force['6. Blunt Impact'] += count['bike']
    force['1. Officer Presence'] += count['body-cam']
    force['1. Officer Presence'] += count['bystander']
    force['1. Officer Presence'] += count['celebrity']
    force['1. Officer Presence'] += count['child']
    force['4. Soft Technique'] += count['choke']
    force['2. Nonthreatening Commands'] += count['conceal']
    force['9. Lethal'] += count['death']
    force['6. Blunt Impact'] += count['dog']
    force['6. Blunt Impact'] += count['drive']
    force['1. Officer Presence'] = count['elderly']
    force['9. Lethal'] += count['explosive']
    force['6. Blunt Impact'] += count['foam-bullet']
    force['7. Chemical'] += count['gas']
    force['4. Soft Technique'] += count['grab']
    force['9. Lethal'] += count['gun']
    force['4. Soft Technique'] += count['headlock']
    force['2. Nonthreatening Commands'] += count['hide-badge']
    force['1. Officer Presence'] += count['homeless']
    force['6. Blunt Impact'] += count['horse']
    force['3. Threatening Commands'] += count['incitement']
    force['3. Threatening Commands'] += count['inhumane-treatment']
    force['1. Officer Presence'] += count['journalist']
    force['5. Hard Technique'] += count['kick']
    force['5. Hard Technique'] += count['knee']
    force['5. Hard Technique'] += count['knee-on-neck']
    force['1. Officer Presence'] += count['legal-observer']
    force['6. Blunt Impact'] += count['less-lethal'] // 3
    force['7. Chemical'] += count['less-lethal'] // 3
    force['8. Conducted Enery Devices'] += count['less-lethal'] // 3
    force['1. Officer Presence'] += count['lgbtq+']
    force['9. Lethal'] += count['live-round']
    force['8. Conducted Enery Devices'] += count['lrad']
    force['7. Chemical'] += count['mace']
    force['6. Blunt Impact'] += count['marking-round']
    force['1. Officer Presence'] += count['medic']
    force['1. Officer Presence'] += count['non-protest']
    force['7. Chemical'] += count['pepper-ball']
    force['7. Chemical'] += count['pepper-spray']
    force['1. Officer Presence'] += count['person-with-disability']
    force['1. Officer Presence'] += count['politician']
    force['1. Officer Presence'] += count['pregnant']
    force['6. Blunt Impact'] += count['projectile']
    force['6. Blunt Impact'] += count['property-destruction']
    force['1. Officer Presence'] += count['protester']
    force['5. Hard Technique'] += count['punch']
    force['5. Hard Technique'] += count['push']
    force['2. Nonthreatening Commands'] += count['racial-profiling']
    force['6. Blunt Impact'] += count['rubber-bullet']
    force['1. Officer Presence'] += count['sexual-assault']
    force['6. Blunt Impact'] += count['shield']
    force['9. Lethal'] += count['shoot']
    force['5. Hard Technique'] += count['shove']
    force['7. Chemical'] += count['spray']
    force['5. Hard Technique'] += count['strike']
    force['8. Conducted Enery Devices'] += count['stun-grenade']
    force['5. Hard Technique'] += count['tackle']
    force['8. Conducted Enery Devices'] += count['tase']
    force['8. Conducted Enery Devices'] += count['taser']
    force['7. Chemical'] += count['tear-gas']
    force['7. Chemical'] += count['tear-gas-canister']
    force['3. Threatening Commands'] += count['threaten']
    force['5. Hard Technique'] += count['throw']
    force['6. Blunt Impact'] += count['vehicle']
    force['6. Blunt Impact'] += count['wooden-bullet']
    force['4. Soft Technique'] += count['zip-tie']

    return force
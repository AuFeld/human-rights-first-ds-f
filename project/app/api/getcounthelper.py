import pandas as pd
import numpy as np

def helper(df):
    count = {}
    for set_of_tags in df["tags"]:
        for tag in set_of_tags:
            if tag in count:
                count[tag] += 1
            else:
                count[tag] = 1
    columns = ['1. Officer Presence', '2. Nonthreatening Commands', '3. Threatening Commands', '4. Soft Technique', '5. Hard Technique', '6. Blunt Impact', '7. Chemical', '8. Conducted Enery Devices', '9. Lethal']
    force = pd.DataFrame(data = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0]]), columns = columns)

    force['2. Nonthreatening Commands'][0] += count['abuse-of-power']
    force['3. Threatening Commands'][0] += count['arrest']
    force['6. Blunt Impact'][0] += count['baton']
    force['6. Blunt Impact'][0] += count['bean-bag']
    force['5. Hard Technique'][0] += count['beat']
    force['6. Blunt Impact'][0] += count['bike']
    force['1. Officer Presence'][0] += count['body-cam']
    force['1. Officer Presence'][0] += count['bystander']
    force['1. Officer Presence'][0] += count['celebrity']
    force['1. Officer Presence'][0] += count['child']
    force['4. Soft Technique'][0] += count['choke']
    force['2. Nonthreatening Commands'][0] += count['conceal']
    force['9. Lethal'][0] += count['death']
    force['6. Blunt Impact'][0] += count['dog']
    force['6. Blunt Impact'][0] += count['drive']
    force['1. Officer Presence'][0] = count['elderly']
    force['9. Lethal'][0] += count['explosive']
    force['6. Blunt Impact'][0] += count['foam-bullet']
    force['7. Chemical'][0] += count['gas']
    force['4. Soft Technique'][0] += count['grab']
    force['9. Lethal'][0] += count['gun']
    force['4. Soft Technique'][0] += count['headlock']
    force['2. Nonthreatening Commands'][0] += count['hide-badge']
    force['1. Officer Presence'][0] += count['homeless']
    force['6. Blunt Impact'][0] += count['horse']
    force['3. Threatening Commands'][0] += count['incitement']
    force['3. Threatening Commands'][0] += count['inhumane-treatment']
    force['1. Officer Presence'][0] += count['journalist']
    force['5. Hard Technique'][0] += count['kick']
    force['5. Hard Technique'][0] += count['knee']
    force['5. Hard Technique'][0] += count['knee-on-neck']
    force['1. Officer Presence'][0] += count['legal-observer']
    force['6. Blunt Impact'][0] += count['less-lethal'] // 3
    force['7. Chemical'][0] += count['less-lethal'] // 3
    force['8. Conducted Enery Devices'][0] += count['less-lethal'] // 3
    force['1. Officer Presence'][0] += count['lgbtq+']
    force['9. Lethal'][0] += count['live-round']
    force['8. Conducted Enery Devices'][0] += count['lrad']
    force['7. Chemical'][0] += count['mace']
    force['6. Blunt Impact'][0] += count['marking-round']
    force['1. Officer Presence'][0] += count['medic']
    force['1. Officer Presence'][0] += count['non-protest']
    force['7. Chemical'][0] += count['pepper-ball']
    force['7. Chemical'][0] += count['pepper-spray']
    force['1. Officer Presence'][0] += count['person-with-disability']
    force['1. Officer Presence'][0] += count['politician']
    force['1. Officer Presence'][0] += count['pregnant']
    force['6. Blunt Impact'][0] += count['projectile']
    force['6. Blunt Impact'][0] += count['property-destruction']
    force['1. Officer Presence'][0] += count['protester']
    force['5. Hard Technique'][0] += count['punch']
    force['5. Hard Technique'][0] += count['push']
    force['2. Nonthreatening Commands'][0] += count['racial-profiling']
    force['6. Blunt Impact'][0] += count['rubber-bullet']
    force['1. Officer Presence'][0] += count['sexual-assault']
    force['6. Blunt Impact'][0] += count['shield']
    force['9. Lethal'][0] += count['shoot']
    force['5. Hard Technique'][0] += count['shove']
    force['7. Chemical'][0] += count['spray']
    force['5. Hard Technique'][0] += count['strike']
    force['8. Conducted Enery Devices'][0] += count['stun-grenade']
    force['5. Hard Technique'][0] += count['tackle']
    force['8. Conducted Enery Devices'][0] += count['tase']
    force['8. Conducted Enery Devices'][0] += count['taser']
    force['7. Chemical'][0] += count['tear-gas']
    force['7. Chemical'][0] += count['tear-gas-canister']
    force['3. Threatening Commands'][0] += count['threaten']
    force['5. Hard Technique'][0] += count['throw']
    force['6. Blunt Impact'][0] += count['vehicle']
    force['6. Blunt Impact'][0] += count['wooden-bullet']
    force['4. Soft Technique'][0] += count['zip-tie']

    return force
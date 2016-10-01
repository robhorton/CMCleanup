
# coding: utf-8

# In[4]:

BatchList = []
CampaignList = []

fileCampaignList = "c:\dvbcampaignlist.xml"
fileBatchList = "c:\dvbbatchlist.xml"


# In[5]:

# Open the campaign file #
import xml.etree.ElementTree as ET
tree = ET.parse(fileCampaignList)
root = tree.getroot()


# In[6]:

# Get the campaign count #
for campaign in root.iter('campaignCount'):
    campaigncount = campaign.text
    print (campaign.text)


# In[7]:

for campaigns in root.iter('name'):
    print (campaigns.text)
    CampaignList.append(campaigns.text)


# In[8]:

# Open the batches #
tree = ET.parse(fileBatchList)
root = tree.getroot()


# In[9]:

for active in root.iter('active'):
    print (active.attrib['count'])


# In[10]:

for batches in root.iter('batch'):
    print (batches.attrib['name'])
    BatchList.append(batches.attrib['name'])


# In[11]:

c = set(CampaignList)
temp3 = [x for x in BatchList if x not in c]

print ('\n'.join(temp3))


# In[12]:

# Remove any batches that do not exist in the campaign list #
for campaign in CampaignList:
    for batch in BatchList:
        if batch != campaign:
               break
    print (campaign)




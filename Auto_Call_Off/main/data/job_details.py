# If you need to update this, please follow these instructions very carefully:
# First you need to understand the basic structure of the dictionary.
# "jobDetails" is the top level of the dictionary. This contains all the names
# of the developers. Each developer name contains a smaller dictionary, with
# names for each of the sites pertaining to that developer. Each level of the
# dictionary has been indented to try to make it clearer how it is structured.
# Each site contains a list of information in the following order: job number
# (only the first half up to and including the hyphen), the name of the
# contracts manager, and an abbreviation for the site. Each item in the
# dictionary must end with a comma, except for the last item. This means that
# after each site, the closing square bracket must be followed by a comma,
# except the last site. Likewise, after each devloper, the closing curly
# bracket must be followed by a comma, except for the last developer.

# Add a new developer:
# Step 1. Find where in the list of developers the new developer would go
# alphabetically.
# Step 2. Find the closing bracket of the developer that will come immediately
# before the new one.
# Step 3. Press enter to make a new line after this one.
# Step 4. Copy and paste the following template (make sure to remove the "#"
# at the beginning of each line):
# "Developer Name": {
#       "Site Name": ["000-", "Contracts Manager", "Dev-Ste"]
# }
# (You may need to add indentations to make it line up with the rest of the
# dictionary)
# Step 5. Edit the information in the template to suit your needs. You can add as
# many sites as you like, just make sure to end each one except the last with a
# comma
# Step 6. Unless this is the last developer in the list, make sure to place a
# comma after the closing curly bracket. Likewise, if the previous developer was 
# the last in the list before, add a comma after its closing curly bracket.
# Step 7. Save the file and follow the instructions for compiling the application.

# Add a new site:
# Step 1. Find the developer of the new site, and find where in the existing list
# of sites the new one will go alphabetically.
# Step 2. Create a new line for the new site.
# Step 3. Copy and past this template (make sure to remove the "#" at the beginning
# of the line):
# "Site Name": ["000-", "Contracts Manager", "Dev-Ste"]
# (You may need to add indentations to make it line up with the rest of the
# dictionary)
# Step 5. Edit the information in the template to suit your needs. You can add as
# many sites as you like, just make sure to end each one except the last with a
# comma

# If you encounter any problems, please try to resolve the issue yourself, carefully
# following the instructions, but if you are unable to solve the issues and need
# help, you can contact me with my e-mail address: vmbaxter@hotmail.co.uk

jobDetails = {
    "BDW": {
        "Compass Point Ph2": ["182-", "Andy Knight", "BDW-CmP"],
        "Forest Walk": ["254-", "Ben Adams", "BDW-FsW"],
        "Harbour Place": ["179-", "Liam Adams", "BDW-HbP"],
        "Niveus Walk": ["181-", "Andy Knight", "BDW-NvW"],
        "Quarter Jack Park": ["175-", "Andy Knight", "BDW-QJP"],
        "SGG Ph2A": ["180-", "Pete Bundy", "BDW-SGG2A"]
    },
    "Bellway": {
        "Blandford Ph1": ["713-", "Andy Knight", "Bel-Bfd1"],
        "Blandford Ph2": ["715-", "Andy Knight", "Bel-Bfd2"],
        "Blandford Ph3": ["716-", "Andy Knight", "Bel-Bfd3"],
        "Boorley Gardens": ["718-", "Andy Knight", "Bel-BlG"],
        "Sherfield on Loddon": ["717-", "Chris Matthews", "Bel-SoL"],
        "Sturminster": ["719-", "Chris Matthews", "Bel-Sms"]
    },
    "Bloor Homes": {
        "Boorley Green": ["736-", "Ben Adams", "Blr-BlG"]
    },
    "Bovis Homes": {
        "WHF 3C": ["6006-", "Ben Gough", "Bvs-WHF3C"]
    },
    "Cala Homes": {
        "Alton": ["512-", "Chris Matthews", "Cal-Atn"]
    },
    "Dandara": {
        "Fontwell Ph2": ["7103-", "Ben Gough", "Ddr-Fwl2"],
        "Yapton": ["7102-", "Ben Gough", "Ddr-Ypt"]
    },
    "Drew Smith": {
        "Kingston Prison": ["459-", "", "Drw-KgP"],
        "Pagham": ["443-", "Ben Adams", "Drw-Pgm"]
    },
    "Foreman Homes": {
        "Alton Ph2": ["6009-", "Ben Adams", "FmH-Atn2"],
        "Whiteley": ["6008-", "Ben Adams", "FmH-Wtl"]
    },
    "Hampshire Homes": {
        "Fontwell": ["9007-", "Ben Gough", "HpH-Fwl"],
        "Titchfield": ["9009-", "Ben Adams", "HpH-Fwl"]
    },
    "Hill Development": {
        "Amber House": ["8005-", "Paul Smithson", "Hil-AbH"],
        "North Town": ["8004-", "Steve Jordan", "Hil-NrT"]
    },
    "Inland Homes": {
        "Meridian Block C": ["3009-", "Reg Noyce", "IlH-Mrd"]
    },
    "Linden Homes": {
        "Alderbury": ["356-", "Andy Knight", "Ldn-Adb"],
        "Boorley PhB4": ["355-", "Ben Adams", "Ldn-BrlB4"],
        "WHF Ph3C": ["354-", "Ben Gough", "Ldn-WHF3C"],
        "WHF Ph5G": ["357-", "Ben Gough", "Ldn-WHF5G"],
        "WHF Ph6I": ["358-", "Ben Gough", "Ldn-WHF6I"],
        "Whiteley": ["353-", "Ben Adams", "Ldn-Wtl"]
    },
    "Places For People": {
        "Poundbury": ["115-", "Chris Matthews", "PFP-Pby"]
    },
    "Questmap": {
        "Ryde": ["116-", "Steve Jordan", "QMp-Rde"]
    },
    "Redrow": {
        "New Fields": ["7011-", "Chris Matthews", "Rdr-NFd"],
        "Windmill Views": ["7012-", "Chris Matthews", "Rdr-WmV"]
    },
    "Taylor Wimpey": {
        "Broadleaf Park": ["4056-", "Ben Adams", "TlW-BlP"],
        "Shopwhyke Lakes": ["4058-", "Ben Adams", "TlW-SwL"],
        "Westergate": ["4053-", "Ben Adams", "TlW-Wtg"]
    }
}

# Old
# BDW
        # "Bordon": ["177-", "Liam Adams", "BDW-Brd"],
        # "Canford Paddock": ["171-", "Andy Knight", "BDW-CfP"],
        # "Madgwick Park": ["172-", "Liam Adams", "BDW-MwP"],
        # "Park Prewett": ["251-", "Chris Matthews", "BDW-PPw"],
        # "SGG Ph2B": ["178-", "Pete Bundy", "BDW-SGG2B"]
# Bellway
        # "Salisbury": ["714-", "Andy Knight", "Bel-Slb"],
# Cala
        # "Liss": ["511-", "Chris Matthews", "Cal-Lis"],
        # "Deepcut": ["504-", "Chris Matthews", "Cal-Dpc"]
# Crest Nicholson
        # "Arbourfield": ["5019-", "Chris Matthews", "CsN-Abf"]
# Dandara
        # "Fontwell Ph1": ["7101-", "Ben Gough", "Ddr-Fwl1"],
        # "Drayton": ["7100-", "Liam Adams", "Ddr-Dyt"],
# David Wilson
        # "SGG": ["250-", "Pete Bundy", "DWH-SGG"]
# Foreman
        # "Alton": ["6004-", "Chris Matthews", "FmH-Atn"],
# Linden
        # "Boorley PhB6": ["352-", "Ben Adams", "Ldn-BrlB6"],
        # "WHF Ph2B": ["351-", "Ben Adams", "Ldn-WHF2B"],
# McCarthy & Stone
        # "Alton": ["2007-", "Steve Jordan", "McS-Atn"]
# Natta
        # "Huxley Court": ["6010-", "Steve Jordan", "Nat-HxC"]
# Redrow
        # "Harbour Views": ["7013-", "Chris Matthews", "Rdr-HbV"],
        # "Hop Field Place Ph3": ["7008-", "Chris Matthews", "Rdr-HFP"],
        # "Orchids Place": ["7007-", "Chris Matthews", "Rdr-OcP"],
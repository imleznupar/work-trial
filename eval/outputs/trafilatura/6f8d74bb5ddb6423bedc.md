# 

## 

Welcome to the Ubuntu Weekly Newsletter, Issue 945 for the week of May 17 - 23, 2026.

## 

- CVE-2026-46333 (ssh-keysign-pwn) Linux kernel vulnerability mitigations
- PinTheft Linux kernel vulnerability mitigation
- Ubuntu 26.04… ready, set, Summit!
- Ubuntu Summit Around the World
- Ubuntu Pastebin Decommissioning
- Stonking Stingray development opening
- Ubuntu Stats
- Hot in Support
- Rocks Public Journal; 2026-05-19
- Other Meeting Reports
- Upcoming Meetings and Events
- Ubuntu Circles! (LoCo) News
- Jornada d’instal·lació i suport - Resolute Racoon- Barcelona, Ubuntu 26.04
- Ubuntu Circles! (LoCo) Events
- Patch Pilot Hand-off 26.10
- The 2026.05.18 SRU Cycle is started
- Microsoft UEFI CA rotation: What it means for Ubuntu users and vendors
- Migrating remaining System V scripts to systemd services
- Canonical launches Ubuntu Core 26
- What Say You - Meet the Members: Thomas Ward
- Ubuntu Cloud News
- Canonical News
- Featured Audio and Video
- Updates and Security for Ubuntu 22.04, 24.04, 25.10, and 26.04
- And much more!

## 

### 

Luci Stanescu alerts us to a security vulnerability disclosed on May 15, 2026 discovered by Qualys: CVE-2026-46333 and named “ssh-keysign-pwn”. We’re given details of the flaw, told the CVSS 3.1 score is 5.5 and severity Medium. The main purpose of the post however is to help mitigate the impact, which affects all Ubuntu releases (including ESM).

[https://ubuntu.com/blog/ssh-keysign-pwn-linux-vulnerability-fixes-available](https://ubuntu.com/blog/ssh-keysign-pwn-linux-vulnerability-fixes-available)

- CVE-2026-46333: Local Root Privilege Escalation and Credential Disclosure in the Linux Kernel ptrace Path - [https://blog.qualys.com/vulnerabilities-threat-research/2026/05/20/cve-2026-46333-local-root-privilege-escalation-and-credential-disclosure-in-the-linux-kernel-ptrace-path](https://blog.qualys.com/vulnerabilities-threat-research/2026/05/20/cve-2026-46333-local-root-privilege-escalation-and-credential-disclosure-in-the-linux-kernel-ptrace-path)
- PATCH 0/4: CVE-2026-46333 - [https://lists.ubuntu.com/archives/kernel-team/2026-May/167945.html](https://lists.ubuntu.com/archives/kernel-team/2026-May/167945.html)

### 

Luci Stanescu alerts us here about a local privilege escalation security vulnerability named ‘Pin Theft’ disclosed on May 19, 2026. Again we’re given details of the flaw, and told the “default Ubuntu configuration disables the automatic loading of the module affected by this vulnerability”. We’re told this flaw’s CVSS 3.1 score is 7.8 and severity High. We’re given details of what releases are impacted (not all, but impacts 20.04 & later), how to check if we’re impacted and given aid in mitigation.

[https://ubuntu.com/blog/pintheft-linux-kernel-vulnerability-mitigation](https://ubuntu.com/blog/pintheft-linux-kernel-vulnerability-mitigation)

### 

Mauro Gaspari (ilvipero) presents an overview of what to expect in this year’s summit. Featuring Ubuntu Discourse’s front seast participation & your photo thread; he covers live streaming, live chat, and remote activities (pixel-art badges). The music will also have live performances, and lastly is the timetable of events.

[https://discourse.ubuntu.com/t/ubuntu-26-04-ready-set-summit/83018](https://discourse.ubuntu.com/t/ubuntu-26-04-ready-set-summit/83018)

### 

The Ubuntu Summit is approaching us fast, and some LoCo/Circles are planning to organize Ubuntu Summit Extended events :

- Ubuntu Latvia: Ubuntu Summit Extended 26.04 - [https://discourse.ubuntu.com/t/ubuntu-summit-extended-26-04-may-27-28-event-here-in-riga-latvia/79080](https://discourse.ubuntu.com/t/ubuntu-summit-extended-26-04-may-27-28-event-here-in-riga-latvia/79080)
- Ubuntu Nambia: Ubuntu Summit Extended - [https://discourse.ubuntu.com/t/ubuntu-summit-extended/82753](https://discourse.ubuntu.com/t/ubuntu-summit-extended/82753)

### 

Aaron Prisk tells us that Canonical IS is decommissioning Ubuntu Pastebin at the end of May 2026, and thus alerts us to move or update any URLs that use it.

\[aaronprisk\] “UPDATE: The decommission has been pushed back to the end of June.”; in response to user feedback.

[https://discourse.ubuntu.com/t/ubuntu-pastebin-decommissioning/82824](https://discourse.ubuntu.com/t/ubuntu-pastebin-decommissioning/82824)

### 

Florent ‘Skia’ Jacquet writes about the Ubuntu Stonking Stingray (26.10) development cycle being open. We’re told the daily builds are now enabled, and we’re also told of changes related to mailing list, release notes (not on Ubuntu Discourse), Test Observer, and more.

[https://lists.ubuntu.com/archives/ubuntu-devel/2026-May/043570.html](https://lists.ubuntu.com/archives/ubuntu-devel/2026-May/043570.html)

## 

### 

- Open: 136147 (+410)
- Critical: 302 (+3)
- Unconfirmed: 72187 (+337)

As always, the Bug Squad needs more help. If you want to get started, please see: [https://wiki.ubuntu.com/BugSquad](https://wiki.ubuntu.com/BugSquad)

### 

- Swedish: 100.00% (1/1371)
- Albanian: 98.86% (4000/0)
- Ukrainian: 89.36% (37362/1687)
- German: 87.16% (45073/241)
- French: 85.77% (49963/6413)

## 

### 

- Streaming audio across RDP From linux to windows on Ubuntu Studio - ([ttps://discourse.ubuntu.com/t/streaming-audio-across-rdp-from-linux-to-windows-on-ubuntu-studio/82343]
- Latest update NVIDIA drivers - [https://discourse.ubuntu.com/t/latest-update-nvidia-drivers/82600](https://discourse.ubuntu.com/t/latest-update-nvidia-drivers/82600)
- Can rsync break a USB pen? - [https://discourse.ubuntu.com/t/can-rsync-break-a-usb-pen/82834](https://discourse.ubuntu.com/t/can-rsync-break-a-usb-pen/82834)
- Escalating to root permissions - [https://discourse.ubuntu.com/t/escalating-to-root-permissions/82882](https://discourse.ubuntu.com/t/escalating-to-root-permissions/82882)
- Qualcomm Atheros AR956x Wireless Network Adapter works only as Wi-Fi adapter and doesn’t work as bluetooth adapter on Ubuntu 24.04.04 LTS - [https://discourse.ubuntu.com/t/qualcomm-atheros-ar956x-wireless-network-adapter-works-only-as-wi-fi-adapter-and-doesn-t-work-as-bluetooth-adapter-on-ubuntu-24-04-04-lts/82890](https://discourse.ubuntu.com/t/qualcomm-atheros-ar956x-wireless-network-adapter-works-only-as-wi-fi-adapter-and-doesn-t-work-as-bluetooth-adapter-on-ubuntu-24-04-04-lts/82890)

Find more support at: [https://discourse.ubuntu.com/c/support-and-help/306](https://discourse.ubuntu.com/c/support-and-help/306)

### 

- Google Chrome update broken - [https://askubuntu.com/questions/1566925/google-chrome-update-broken](https://askubuntu.com/questions/1566925/google-chrome-update-broken)
- Boomaga is not available in 26.04. What now? - [https://askubuntu.com/questions/1566961/boomaga-is-not-available-in-26-04-what-now](https://askubuntu.com/questions/1566961/boomaga-is-not-available-in-26-04-what-now)
- Ubuntu 26.04: Pipewire pw-play cannot play sound as root from within a script - [https://askubuntu.com/questions/1567035/ubuntu-26-04-pipewire-pw-play-cannot-play-sound-as-root-from-within-a-script](https://askubuntu.com/questions/1567035/ubuntu-26-04-pipewire-pw-play-cannot-play-sound-as-root-from-within-a-script)
- How to adapt apt\_repository in ansible in Ubuntu 26.04 - [https://askubuntu.com/questions/1566955/how-to-adapt-apt-repository-in-ansible-in-ubuntu-26-04](https://askubuntu.com/questions/1566955/how-to-adapt-apt-repository-in-ansible-in-ubuntu-26-04)
- Unable to install Steam necessary 32-bit drivers? - [https://askubuntu.com/questions/1567026/unable-to-install-steam-necessary-32-bit-drivers](https://askubuntu.com/questions/1567026/unable-to-install-steam-necessary-32-bit-drivers)

Ask (and answer!) questions at: [https://askubuntu.com/](https://askubuntu.com/)

## 

### 

The Python3.14 rock is now available in Docker Hub and ECR. Also, find our newest blog at [https://discourse.charmhub.io/t/when-the-resolute-raccoon-meets-the-medusa-build-the-ubuntu-oci-image-as-a-rock/20309](https://discourse.charmhub.io/t/when-the-resolute-raccoon-meets-the-medusa-build-the-ubuntu-oci-image-as-a-rock/20309) . Finally, the [OSV scanner is about to gain the ability to scan chiseled containers](https://github.com/google/osv-scanner/pull/2772)!

## 

- \[daily\] Server Triage Reports - [https://discourse.ubuntu.com/c/project/server/17](https://discourse.ubuntu.com/c/project/server/17)
- Foundations Team Updates - 2026-05-21 - [https://discourse.ubuntu.com/t/foundations-team-updates-2026-05-21/82706](https://discourse.ubuntu.com/t/foundations-team-updates-2026-05-21/82706)

## 

- Starcraft Clinics (2nd option): Monday 25 May, 11:00 - 11:50 AM - [https://discourse.ubuntu.com/t/starcraft-clinics-2nd-option/48031](https://discourse.ubuntu.com/t/starcraft-clinics-2nd-option/48031) | [https://meet.google.com/ixc-nucm-hjn](https://meet.google.com/ixc-nucm-hjn)
- Rocks Community monthly meetings (Virtual): Tuesday, 26 May, 2:00 AM - 3:00 PM CET - [https://discourse.ubuntu.com/t/rocks-community-monthly-meetings-virtual/48191](https://discourse.ubuntu.com/t/rocks-community-monthly-meetings-virtual/48191) | [https://meet.google.com/hfe-fbky-vnh](https://meet.google.com/hfe-fbky-vnh)
- Ubuntu HPC weekly community call: Wednesday, 27 May, 16:30 - 17:00 - [https://meet.jit.si/Ubuntu-HPC](https://meet.jit.si/Ubuntu-HPC) | [https://matrix.to/#/#hpc:ubuntu.com](https://matrix.to/#/#hpc:ubuntu.com)
- Ubuntu Summit 26.04: Online: 27 - 28 May - \< [Ubuntu Summit | Ubuntu](https://ubuntu.com/summit)>
- UbuCon Asia x COSCUP 2026 Team meeting: 27 May, 12:30 - [https://discourse.ubuntu.com/t/ubucon-asia-x-coscup-2026-team-meeting-2026-04-29-12-00-utc/81741](https://discourse.ubuntu.com/t/ubucon-asia-x-coscup-2026-team-meeting-2026-04-29-12-00-utc/81741)
- Lubuntu Weekly Standup: Thursday 28 May, 9:00 - 10:00 PM - [https://matrix.to/#/#lubuntu-devel:ubuntu.com](https://matrix.to/#/#lubuntu-devel:ubuntu.com) | [https://discourse.ubuntu.com/t/lubuntu-weekly-standup/43699](https://discourse.ubuntu.com/t/lubuntu-weekly-standup/43699)
- Documentation Community Hour: fri, 29 May, 4:00 - 5:00 PM BST - [https://discourse.ubuntu.com/t/community-hour/42771](https://discourse.ubuntu.com/t/community-hour/42771) | [https://meet.google.com/zcy-onjk-smi](https://meet.google.com/zcy-onjk-smi)
- Ubuntu 26.04 LTS Release Party @ Taipei: 摩茲工寮 Mozilla Community Space Taipei; Sat, 30 May, 2:30 PM - 5:30 PM (Taipei) - [https://discourse.ubuntu.com/t/ubuntu-26-04-lts-release-party-taipei/81876](https://discourse.ubuntu.com/t/ubuntu-26-04-lts-release-party-taipei/81876) | \<[摩茲工寮 Mozilla Community Space Taipei | MozTW, Mozilla Taiwan Community](https://moztw.org/space/))

Times shown are UTC unless otherwise specified. For more details and further dates please visit: [https://ubuntu.com/community](https://ubuntu.com/community) | [https://discourse.ubuntu.com/upcoming-events](https://discourse.ubuntu.com/upcoming-events)

## 

### 

Walter Garcia Fontes reminds us (in Catalan) that Ubuntu 26.04 has been published, and alerts us to an organized day of installation and support run by the Ubuntu community in Catalan. We’re told the day (June 6) and time, where, and given links for more, including to register for this event.

## 

The following LoCo team events are currently scheduled in the next two weeks:

- Arizona LoCo: Virtual Tempe Ubuntu Hour on line; 28 May, 1900 - 2000 - BigBlue Button, [https://bbb.azloco.net](https://bbb.azloco.net)
- Ubuntu-pt: Monthly Meetup @ Sintra; Thu, 28 May 8:00 PM - 10:30 PM (Lisbon) - [https://discourse.ubuntu.com/t/2026-04-23-ubuntu-pt-monthly-meetup-sintra/82921](https://discourse.ubuntu.com/t/2026-04-23-ubuntu-pt-monthly-meetup-sintra/82921) | [https://discourse.ubuntu.com/t/2026-05-28-encontro-ubuntu-pt-de-maio-sintra/82923](https://discourse.ubuntu.com/t/2026-05-28-encontro-ubuntu-pt-de-maio-sintra/82923)
- Atlanta Linux Enthusiasts: Linux Help Session (Online) - Jitsi; 31 May, 2 PM CT - [https://www.heylo.com/event/e13ea155-e713-477a-a59e-55795c3b1f11](https://www.heylo.com/event/e13ea155-e713-477a-a59e-55795c3b1f11)
- Arizona LoCo: Virtual Tempe Ubuntu Hour on line; 04 June, 1900 - 2000 - BigBlue Button, [https://bbb.azloco.net](https://bbb.azloco.net)
- Arizona LoCo: Virtual Installfest/Linux Workshop on line; 06 June, 1000-1600 - Big Blue Button, [https://bbb.azloco.net](https://bbb.azloco.net) (co-hosted with the Phoenix Linux User Group)
- Arizona LoCo: AZLOCO Team Meeting on IRC.libera.chat; 07 June, 2100-2130 - IRC channel [ubuntu](https://discourse.ubuntu.com/tag/ubuntu).us.az

Looking beyond the next two weeks? Visit the respective Circles!/LoCo Team calendar to browse upcoming events.

Please also see:

- Ubuntu Arizona LoCo: [https://discourse.ubuntu.com/t/upcoming-events-for-azloco/38466](https://discourse.ubuntu.com/t/upcoming-events-for-azloco/38466)
- Ubuntu-pt LoCo: [https://discourse.ubuntu.com/c/locos/ubuntu-pt/132](https://discourse.ubuntu.com/c/locos/ubuntu-pt/132)
- Atlanta Linux Enthusiasts: [https://ale.org/](https://ale.org/)
- Registered LoCo contacts: [https://discourse.ubuntu.com/c/locos/129](https://discourse.ubuntu.com/c/locos/129)

## 

### 

Florent ‘Skia’ Jacquet starts the Patch Pilot Program for the Ubuntu 26.10 cycle. With details of the thread, he reminds us to post on the thread only if you’re posting a hand-off report. We’re given links to the latest and prior hand-off posts.

[https://discourse.ubuntu.com/t/patch-pilot-hand-off-26-10/82594](https://discourse.ubuntu.com/t/patch-pilot-hand-off-26-10/82594)

### 

Edoardo Canepa posts some details of the 18-May through 21-June five week SRU cycle, and also 22-June through 19-July four week SRU cycle.

[https://discourse.ubuntu.com/t/the-2026-05-18-sru-cycle-is-started/82596](https://discourse.ubuntu.com/t/the-2026-05-18-sru-cycle-is-started/82596)

### 

This blog (Jon Seager and Julian Andres Klode) addresses the issue that Microsoft 2011 UEFI and KEK CA’s are set to expire in June 2026, being replaced by 2023 CAs. This comprehensive blog post gives us details of this change, and will be useful for existing Ubuntu users, Canonical-supplied VMs, and device vendors using Ubuntu.

- Secure Boot and Microsoft CA Rollover - a heads-up for distributions - [https://blog.einval.com/2026/05/22#secure\_boot\_ca\_rollover](https://blog.einval.com/2026/05/22#secure_boot_ca_rollover)

### 

Nick (enr0n) Rosbrook writes that some Ubuntu packages still ship System V scripts in them, something which won’t be available in Ubuntu 26.10 due to removal of systemd-sysv-generator in systemd v260. Nick highlights that upstream Debian has more time before Debian 14 (forky) releases than Ubuntu does with Ubuntu 26.10, and thus gives clues on what needs to be done this 26.10 cycle.

[https://discourse.ubuntu.com/t/migrating-remaining-system-v-scripts-to-systemd-services/82757](https://discourse.ubuntu.com/t/migrating-remaining-system-v-scripts-to-systemd-services/82757)

### 

This post tells us about Canonical’s release of Ubuntu Core 26. We’re told what it is and why we’d want it, including quotes from various people including such as from Jon Seager, the VP of Ubuntu Engineering. Some of the improvements, such as faster over-the-air updates are mentioned, with links so we can learn more, or should we want to build our own image right now. This is an extensive post.

[https://canonical.com/blog/canonical-launches-ubuntu-core-26](https://canonical.com/blog/canonical-launches-ubuntu-core-26)

- Canonical Launches Ubuntu Core 26, Its Latest Snap-Powered Immutable Operating System - [https://www.hackster.io/news/canonical-launches-ubuntu-core-26-its-latest-snap-powered-immutable-operating-system-d641fda6e2bc](https://www.hackster.io/news/canonical-launches-ubuntu-core-26-its-latest-snap-powered-immutable-operating-system-d641fda6e2bc)>
- Canonical Launches Ubuntu Core 26 with Live Kernel Patching, Optimized Updates - [https://9to5linux.com/canonical-launches-ubuntu-core-26-with-live-kernel-patching-optimized-updates](https://9to5linux.com/canonical-launches-ubuntu-core-26-with-live-kernel-patching-optimized-updates)
- A look into Ubuntu Core 26: Cloud-powered edge computing with AWS IoT Greengrass and Azure IoT Edge - [https://ubuntu.com//blog/ubuntu-core-26-cloud-integration](https://ubuntu.com//blog/ubuntu-core-26-cloud-integration)
- Ubuntu Core 26 offers an immutable Linux you can trust through 2041 - [https://www.zdnet.com/article/ubuntu-core-26-canonicals-minimal-immutable-operating-system-arrives/](https://www.zdnet.com/article/ubuntu-core-26-canonicals-minimal-immutable-operating-system-arrives/)

## 

### 

“I initially got involved in the Ubuntu community by needing support with Ubuntu 9.04 initially. That was my first introduction into the Ubuntu community. However, as I learned Linux and got more familiar with administration of the system and the nitty-gritty of Ubuntu and programming and packages, I began to get involved with Ask Ubuntu, helping users with issues and asking and answering questions in the Ask Ubuntu web space. That slowly expanded into development and technical side of things in Ubuntu (such as package maintenance, development, etc.)”

[https://discourse.ubuntu.com/t/meet-the-members-thomas-ward/82587](https://discourse.ubuntu.com/t/meet-the-members-thomas-ward/82587)

## 

- Canonical announces fully Managed Kubeflow AI operations platform on the Microsoft Azure Marketplace - [https://ubuntu.com//blog/managed-kubeflow-microsoft-azure-canonical-release](https://ubuntu.com//blog/managed-kubeflow-microsoft-azure-canonical-release)

## 

- Developing web apps with local LLM inference - [https://ubuntu.com/blog/developing-web-apps-with-local-llm-inference](https://ubuntu.com/blog/developing-web-apps-with-local-llm-inference)
- Decoding design: How design and engineering thrive together in open source - [https://ubuntu.com//blog/decoding-design-how-design-and-engineering-thrive-together-in-open-source](https://ubuntu.com//blog/decoding-design-how-design-and-engineering-thrive-together-in-open-source)

## 

### 

“Estivemos em Coimbra de 15 a 17 de Maio, para visitar a WikiCon 2026 e celebrar os 25 anos do universo Wikimedia! No último dia da Wikicon conversámos com alguns membros da organização; Joaquim Santos, (que trabalhou no Herbário da Universidade de Coimbra), Waldir Pimenta e André Barbosa, da Associação Wikimedia Portugal. Falámos sobre as pontes entre as comunidades de software livre e wikimedistas, os desafios do conhecimento livre e construído em comunidade, as dificuldades para resolver problemas de taxonomia, catalogação e ciência cidadã - mas também como a magia das comunidades resolve (quase) tudo. A gravação…informal, foi feita com microfones muito valentes e abnegados.”

[https://podcastubuntuportugal.org/e380/](https://podcastubuntuportugal.org/e380/)

## 

### 

- \[USN-8273-1\] Linux kernel vulnerabilities - [\[USN-8273-1\] Linux kernel vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010561.html)
- \[USN-8274-1\] Linux kernel vulnerabilities - [\[USN-8274-1\] Linux kernel vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010562.html)
- \[USN-8254-3\] Linux kernel (NVIDIA Tegra) vulnerabilities - [\[USN-8254-3\] Linux kernel (NVIDIA Tegra) vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010563.html)
- \[USN-8255-3\] Linux kernel vulnerabilities - [\[USN-8255-3\] Linux kernel vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010564.html)
- \[USN-8275-1\] Linux kernel (Xilinx ZynqMP) vulnerabilities - [\[USN-8275-1\] Linux kernel (Xilinx ZynqMP) vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010565.html)
- \[USN-8272-1\] Smarty vulnerability - [\[USN-8272-1\] Smarty vulnerability](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010566.html)
- \[USN-8276-1\] Highlight.js vulnerability - [\[USN-8276-1\] Highlight.js vulnerability](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010567.html)
- \[USN-8277-1\] Linux kernel vulnerabilities - [\[USN-8277-1\] Linux kernel vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010572.html)
- \[USN-8278-1\] Linux kernel vulnerabilities - [\[USN-8278-1\] Linux kernel vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010570.html)
- \[USN-8279-1\] Linux kernel vulnerabilities - [\[USN-8279-1\] Linux kernel vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010568.html)
- \[USN-8280-1\] Linux kernel vulnerabilities - [\[USN-8280-1\] Linux kernel vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010569.html)
- \[USN-8281-1\] Linux kernel vulnerabilities - [\[USN-8281-1\] Linux kernel vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010571.html)
- \[USN-8286-1\] OpenVPN vulnerabilities - [\[USN-8286-1\] OpenVPN vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010574.html)
- \[USN-8285-1\] GStreamer Good Plugins vulnerability - [\[USN-8285-1\] GStreamer Good Plugins vulnerability](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010575.html)
- \[USN-8284-1\] GnuTLS vulnerabilities - [\[USN-8284-1\] GnuTLS vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010573.html)
- \[USN-8283-1\] rsync vulnerabilities - [\[USN-8283-1\] rsync vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010576.html)
- \[USN-8282-1\] Unbound vulnerabilities - [\[USN-8282-1\] Unbound vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010577.html)
- \[USN-8289-1\] Linux kernel (NVIDIA) vulnerabilities - [\[USN-8289-1\] Linux kernel (NVIDIA) vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010578.html)
- \[USN-8202-3\] jq regression - [\[USN-8202-3\] jq regression](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010579.html)
- \[USN-8291-1\] Linux kernel (Intel IoTG Real-time) vulnerabilities - [\[USN-8291-1\] Linux kernel (Intel IoTG Real-time) vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010580.html)
- \[USN-8287-1\] XDG Desktop Portal vulnerability - [\[USN-8287-1\] XDG Desktop Portal vulnerability](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010581.html)
- \[USN-8288-1\] Bubblewrap vulnerability - [\[USN-8288-1\] Bubblewrap vulnerability](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010582.html)
- \[USN-8292-1\] libarchive vulnerabilities - [\[USN-8292-1\] libarchive vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010583.html)
- \[USN-8293-1\] Bind vulnerabilities - [\[USN-8293-1\] Bind vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010584.html)
- \[USN-8294-1\] PostgreSQL vulnerabilities - [\[USN-8294-1\] PostgreSQL vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010585.html)
- \[USN-8295-1\] Evince vulnerability - [\[USN-8295-1\] Evince vulnerability](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010586.html)
- \[USN-8277-2\] Linux kernel (Oracle) vulnerabilities - [\[USN-8277-2\] Linux kernel (Oracle) vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010587.html)
- \[USN-8291-2\] Linux kernel (Low Latency) vulnerabilities - [\[USN-8291-2\] Linux kernel (Low Latency) vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010588.html)
- \[USN-8296-1\] Linux kernel (FIPS) vulnerabilities - [\[USN-8296-1\] Linux kernel (FIPS) vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010589.html)
- \[USN-8290-1\] Path-to-Regexp vulnerability - [\[USN-8290-1\] Path-to-Regexp vulnerability](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010590.html)
- \[USN-8297-1\] Linux kernel (GCP) vulnerabilities - [\[USN-8297-1\] Linux kernel (GCP) vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010591.html)
- \[USN-8279-2\] Linux kernel (GCP) vulnerabilities - [\[USN-8279-2\] Linux kernel (GCP) vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010592.html)
- \[USN-8280-2\] Linux kernel (Azure)vulnerabilities - [\[USN-8280-2\] Linux kernel (Azure)vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010594.html)
- \[USN-8281-2\] Linux kernel (Azure) vulnerabilities - [\[USN-8281-2\] Linux kernel (Azure) vulnerabilities](https://lists.ubuntu.com/archives/ubuntu-security-announce/2026-May/010593.html)

### 

- fabric-manager-535 535.309.01-0ubuntu0.22.04.1 - [\[ubuntu/jammy-updates\] fabric-manager-535 535.309.01-0ubuntu0.22.04.1 (Accepted)](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046320.html)
- fabric-manager-580 580.159.03-0ubuntu0.22.04.1 - [\[ubuntu/jammy-updates\] fabric-manager-580 580.159.03-0ubuntu0.22.04.1 (Accepted)](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046321.html)
- libnvidia-nscq-535 535.309.01-0ubuntu0.22.04.1 - [\[ubuntu/jammy-updates\] libnvidia-nscq-535 535.309.01-0ubuntu0.22.04.1 (Accepted)](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046322.html)
- fabric-manager-595 595.71.05-0ubuntu0.22.04.1 - [\[ubuntu/jammy-updates\] fabric-manager-595 595.71.05-0ubuntu0.22.04.1 (Accepted)](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046323.html)
- libnvidia-nscq-580 580.159.03-0ubuntu0.22.04.1 - [\[ubuntu/jammy-updates\] libnvidia-nscq-580 580.159.03-0ubuntu0.22.04.1 (Accepted)](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046324.html)
- libnvidia-nscq-595 595.71.05-0ubuntu0.22.04.1 - [\[ubuntu/jammy-updates\] libnvidia-nscq-595 595.71.05-0ubuntu0.22.04.1 (Accepted)](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046325.html)
- nvidia-imex-580 580.159.03-0ubuntu0.22.04.2 - [\[ubuntu/jammy-updates\] nvidia-imex-580 580.159.03-0ubuntu0.22.04.2 (Accepted)](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046326.html)
- nvidia-imex-595 595.71.05-0ubuntu0.22.04.1 - [\[ubuntu/jammy-updates\] nvidia-imex-595 595.71.05-0ubuntu0.22.04.1 (Accepted)](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046327.html)
- nvidia-graphics-drivers-580 580.159.03-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046328.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046328.html)
- nvidia-graphics-drivers-595 595.71.05-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046329.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046329.html)
- nvidia-graphics-drivers-535 535.309.01-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046330.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046330.html)
- nvidia-graphics-drivers-535-server 535.309.01-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046331.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046331.html)
- nvidia-graphics-drivers-580-server 580.159.03-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046332.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046332.html)
- nvidia-graphics-drivers-595-server 595.71.05-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046333.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046333.html)
- linux-restricted-signatures 5.15.0-179.189+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046334.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046334.html)
- linux-restricted-modules 5.15.0-179.189+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046335.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046335.html)
- linux-restricted-signatures-lowlatency 5.15.0-177.187+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046336.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046336.html)
- linux-restricted-modules-lowlatency 5.15.0-177.187+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046337.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046337.html)
- linux-restricted-signatures-hwe-6.8 6.8.0-117.117\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046338.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046338.html)
- linux-restricted-modules-hwe-6.8 6.8.0-117.117\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046339.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046339.html)
- linux-restricted-signatures-lowlatency-hwe-6.8 6.8.0-117.117.1\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046340.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046340.html)
- linux-restricted-modules-lowlatency-hwe-6.8 6.8.0-117.117.1\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046341.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046341.html)
- linux-restricted-modules-aws 5.15.0-1108.115+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046342.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046342.html)
- linux-restricted-signatures-aws-6.8 6.8.0-1055.58\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046343.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046343.html)
- linux-restricted-signatures-aws 5.15.0-1108.115+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046344.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046344.html)
- linux-restricted-modules-aws-6.8 6.8.0-1055.58\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046345.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046345.html)
- linux-restricted-modules-azure 5.15.0-1111.120+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046346.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046346.html)
- linux-restricted-signatures-azure 5.15.0-1111.120+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046347.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046347.html)
- linux-restricted-signatures-azure-6.8 6.8.0-1052.58\~22.04.1+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046348.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046348.html)
- linux-restricted-modules-azure-6.8 6.8.0-1052.58\~22.04.1+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046349.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046349.html)
- linux-restricted-modules-azure-fde-6.8 6.8.0-1053.60\~22.04.1+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046350.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046350.html)
- linux-restricted-signatures-azure-fde-6.8 6.8.0-1053.60\~22.04.1+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046351.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046351.html)
- linux-restricted-signatures-gcp 5.15.0-1108.117+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046352.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046352.html)
- linux-restricted-modules-gcp 5.15.0-1108.117+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046353.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046353.html)
- linux-restricted-signatures-gcp-6.8 6.8.0-1058.61\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046354.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046354.html)
- linux-restricted-modules-gcp-6.8 6.8.0-1058.61\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046355.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046355.html)
- linux-restricted-signatures-ibm-6.8 6.8.0-1055.56\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046356.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046356.html)
- linux-restricted-modules-ibm-6.8 6.8.0-1055.56\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046357.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046357.html)
- linux-restricted-signatures-oracle-6.8 6.8.0-1052.53\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046358.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046358.html)
- linux-restricted-signatures-oracle 5.15.0-1105.111+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046359.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046359.html)
- linux-restricted-modules-oracle-6.8 6.8.0-1052.53\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046360.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046360.html)
- linux-restricted-modules-oracle 5.15.0-1105.111+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046361.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046361.html)
- linux-restricted-signatures-intel-iotg 5.15.0-1103.109+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046362.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046362.html)
- linux-restricted-modules-intel-iotg 5.15.0-1103.109+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046363.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046363.html)
- linux-restricted-signatures-nvidia 5.15.0-1103.104+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046364.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046364.html)
- linux-restricted-modules-nvidia 5.15.0-1103.104+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046365.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046365.html)
- linux-restricted-signatures-nvidia-6.8 6.8.0-1054.57\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046366.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046366.html)
- linux-restricted-modules-nvidia-6.8 6.8.0-1054.57\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046367.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046367.html)
- linux-restricted-modules-nvidia-tegra-igx 5.15.0-1049.49+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046368.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046368.html)
- linux-restricted-signatures-nvidia-tegra-igx 5.15.0-1049.49+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046369.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046369.html)
- linux 5.15.0-179.189 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046370.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046370.html)
- linux-signed 5.15.0-179.189 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046371.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046371.html)
- linux-restricted-signatures 5.15.0-179.189 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046372.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046372.html)
- linux-meta 5.15.0.179.163 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046373.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046373.html)
- linux-restricted-modules 5.15.0-179.189 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046374.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046374.html)
- linux-aws 5.15.0-1108.115 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046375.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046375.html)
- linux-meta-aws 5.15.0.1108.111 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046376.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046376.html)
- linux-signed-aws 5.15.0-1108.115 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046377.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046377.html)
- linux-restricted-modules-aws 5.15.0-1108.115 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046378.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046378.html)
- linux-restricted-signatures-aws 5.15.0-1108.115 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046379.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046379.html)
- linux-gcp 5.15.0-1108.117 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046380.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046380.html)
- linux-meta-gcp 5.15.0.1108.104 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046381.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046381.html)
- linux-signed-gcp 5.15.0-1108.117 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046382.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046382.html)
- linux-restricted-modules-gcp 5.15.0-1108.117 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046383.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046383.html)
- linux-restricted-signatures-gcp 5.15.0-1108.117 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046384.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046384.html)
- linux-meta-gke 5.15.0.1104.103 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046385.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046385.html)
- linux-signed-gke 5.15.0-1104.110 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046386.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046386.html)
- linux-gke 5.15.0-1104.110 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046387.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046387.html)
- linux-meta-gkeop 5.15.0.1091.90 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046388.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046388.html)
- linux-gkeop 5.15.0-1091.99 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046389.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046389.html)
- linux-signed-gkeop 5.15.0-1091.99 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046390.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046390.html)
- linux-meta-ibm 5.15.0.1102.98 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046391.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046391.html)
- linux-signed-ibm 5.15.0-1102.105 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046392.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046392.html)
- linux-ibm 5.15.0-1102.105 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046393.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046393.html)
- linux-meta-intel-iotg 5.15.0.1103.102 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046394.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046394.html)
- linux-signed-intel-iotg 5.15.0-1103.109 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046395.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046395.html)
- linux-intel-iotg 5.15.0-1103.109 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046396.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046396.html)
- linux-restricted-signatures-intel-iotg 5.15.0-1103.109 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046397.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046397.html)
- linux-restricted-modules-intel-iotg 5.15.0-1103.109 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046398.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046398.html)
- linux-signed-kvm 5.15.0-1100.105 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046399.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046399.html)
- linux-meta-kvm 5.15.0.1100.96 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046400.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046400.html)
- linux-kvm 5.15.0-1100.105 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046401.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046401.html)
- linux-meta-nvidia 5.15.0.1103.103 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046403.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046403.html)
- linux-signed-nvidia 5.15.0-1103.104 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046402.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046402.html)
- linux-restricted-signatures-nvidia 5.15.0-1103.104 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046404.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046404.html)
- linux-nvidia 5.15.0-1103.104 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046405.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046405.html)
- linux-restricted-modules-nvidia 5.15.0-1103.104 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046406.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046406.html)
- linux-meta-oracle 5.15.0.1105.101 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046407.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046407.html)
- linux-signed-oracle 5.15.0-1105.111 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046408.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046408.html)
- linux-oracle 5.15.0-1105.111 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046409.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046409.html)
- linux-restricted-signatures-oracle 5.15.0-1105.111 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046410.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046410.html)
- linux-meta-raspi 5.15.0.1102.100 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046411.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046411.html)
- linux-restricted-modules-oracle 5.15.0-1105.111 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046412.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046412.html)
- linux-raspi 5.15.0-1102.105 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046413.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046413.html)
- linux-meta-riscv-6.8 6.8.0.117.117\~22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046414.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046414.html)
- linux-riscv-6.8 6.8.0-117.117\~22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046415.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046415.html)
- linux-nvidia-tegra 5.15.0-1060.60 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046416.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046416.html)
- linux-meta-nvidia-tegra 5.15.0.1060.60 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046417.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046417.html)
- linux-signed-nvidia-tegra 5.15.0-1060.60 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046418.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046418.html)
- linux-meta-ibm-6.8 6.8.0-1055.56\~22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046419.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046419.html)
- linux-signed-ibm-6.8 6.8.0-1055.56\~22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046420.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046420.html)
- linux-restricted-signatures-ibm-6.8 6.8.0-1055.56\~22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046421.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046421.html)
- linux-restricted-modules-ibm-6.8 6.8.0-1055.56\~22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046422.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046422.html)
- linux-ibm-6.8 6.8.0-1055.56\~22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046423.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046423.html)
- linux-signed-lowlatency-hwe-6.8 6.8.0-117.117.1\~22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046424.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046424.html)
- linux-meta-lowlatency-hwe-6.8 6.8.0-117.117.1\~22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046425.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046425.html)
- linux-lowlatency-hwe-6.8 6.8.0-117.117.1\~22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046426.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046426.html)
- linux-restricted-signatures-lowlatency-hwe-6.8 6.8.0-117.117.1\~22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046427.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046427.html)
- linux-restricted-modules-lowlatency-hwe-6.8 6.8.0-117.117.1\~22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046428.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046428.html)
- lintian 2.114.0ubuntu1.8 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046429.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046429.html)
- fabric-manager-535 535.309.01-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046430.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046430.html)
- fabric-manager-570 570.211.01-0ubuntu1.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046431.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046431.html)
- fabric-manager-580 580.159.03-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046432.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046432.html)
- fabric-manager-590 590.48.01-0ubuntu0.22.04.2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046433.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046433.html)
- fabric-manager-595 595.71.05-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046434.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046434.html)
- libnvidia-nscq-535 535.309.01-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046435.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046435.html)
- libnvidia-nscq-570 570.211.01-0ubuntu1.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046436.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046436.html)
- libnvidia-nscq-580 580.159.03-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046437.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046437.html)
- libnvidia-nscq-590 590.48.01-0ubuntu0.22.04.2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046438.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046438.html)
- libnvidia-nscq-595 595.71.05-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046439.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046439.html)
- nvidia-imex-580 580.159.03-0ubuntu0.22.04.2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046440.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046440.html)
- nvidia-imex-570 570.211.01-0ubuntu1.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046441.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046441.html)
- nvidia-imex-590 590.48.01-0ubuntu0.22.04.2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046442.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046442.html)
- nvidia-imex-595 595.71.05-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046443.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046443.html)
- nvidia-graphics-drivers-535 535.309.01-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046444.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046444.html)
- nvidia-graphics-drivers-580 580.159.03-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046445.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046445.html)
- nvidia-graphics-drivers-595 595.71.05-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046446.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046446.html)
- nvidia-graphics-drivers-535-server 535.309.01-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046447.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046447.html)
- nvidia-graphics-drivers-580-server 580.159.03-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046448.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046448.html)
- nvidia-graphics-drivers-595-server 595.71.05-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046449.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046449.html)
- nvidia-graphics-drivers-570 570.211.01-0ubuntu1.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046450.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046450.html)
- nvidia-graphics-drivers-570-server 570.211.01-0ubuntu1.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046451.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046451.html)
- nvidia-graphics-drivers-590 590.48.01-0ubuntu0.22.04.4 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046452.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046452.html)
- nvidia-graphics-drivers-590-server 590.48.01-0ubuntu0.22.04.4 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046453.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046453.html)
- linux-restricted-signatures 5.15.0-179.189+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046454.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046454.html)
- linux-restricted-modules 5.15.0-179.189+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046455.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046455.html)
- linux-restricted-signatures-lowlatency 5.15.0-177.187+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046456.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046456.html)
- linux-restricted-modules-lowlatency 5.15.0-177.187+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046457.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046457.html)
- linux-restricted-signatures-lowlatency-hwe-6.8 6.8.0-117.117.1\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046458.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046458.html)
- linux-restricted-signatures-aws 5.15.0-1108.115+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046459.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046459.html)
- linux-restricted-modules-lowlatency-hwe-6.8 6.8.0-117.117.1\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046460.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046460.html)
- linux-restricted-modules-aws 5.15.0-1108.115+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046461.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046461.html)
- linux-restricted-signatures-azure 5.15.0-1111.120+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046462.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046462.html)
- linux-restricted-modules-azure 5.15.0-1111.120+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046463.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046463.html)
- linux-restricted-signatures-azure-6.8 6.8.0-1052.58\~22.04.1+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046464.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046464.html)
- linux-restricted-modules-azure-6.8 6.8.0-1052.58\~22.04.1+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046465.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046465.html)
- linux-restricted-signatures-gcp 5.15.0-1108.117+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046466.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046466.html)
- linux-restricted-modules-gcp 5.15.0-1108.117+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046467.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046467.html)
- linux-restricted-signatures-ibm-6.8 6.8.0-1055.56\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046468.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046468.html)
- linux-restricted-modules-oracle 5.15.0-1105.111+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046469.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046469.html)
- linux-restricted-signatures-oracle 5.15.0-1105.111+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046470.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046470.html)
- linux-restricted-modules-intel-iotg 5.15.0-1103.109+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046471.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046471.html)
- linux-restricted-signatures-intel-iotg 5.15.0-1103.109+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046472.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046472.html)
- linux-restricted-modules-ibm-6.8 6.8.0-1055.56\~22.04.1+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046473.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046473.html)
- linux-restricted-modules-nvidia 5.15.0-1103.104+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046474.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046474.html)
- linux-restricted-signatures-nvidia 5.15.0-1103.104+1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046475.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046475.html)
- unbound 1.13.1-1ubuntu5.15 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046476.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046476.html)
- rsync 3.2.7-0ubuntu0.22.04.6 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046477.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046477.html)
- gnutls28 3.7.3-4ubuntu1.9 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046478.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046478.html)
- openvpn 2.5.11-0ubuntu0.22.04.3 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046480.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046480.html)
- google-compute-engine-oslogin 20260116.00-0ubuntu1\~22.04.0 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046484.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046484.html)
- google-osconfig-agent 20251028.00-0ubuntu2\~22.04.0 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046485.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046485.html)
- gce-compute-image-packages 20260116.00-0ubuntu1\~22.04.0 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046486.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046486.html)
- linux-restricted-signatures-lowlatency 5.15.0-178.188+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046487.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046487.html)
- linux-restricted-modules-lowlatency 5.15.0-178.188+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046488.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046488.html)
- snapd 2.75.2+ubuntu22.04 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046489.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046489.html)
- libarchive 3.6.0-1ubuntu1.7 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046490.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046490.html)
- linux-meta-lowlatency 5.15.0.178.150 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046491.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046491.html)
- linux-signed-lowlatency 5.15.0-178.188 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046492.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046492.html)
- linux-restricted-signatures-lowlatency 5.15.0-178.188+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046493.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046493.html)
- linux-lowlatency 5.15.0-178.188 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046494.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046494.html)
- linux-restricted-modules-lowlatency 5.15.0-178.188+2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046495.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046495.html)
- bind9 1:9.18.39-0ubuntu0.22.04.4 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046497.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046497.html)
- postgresql-14 14.23-0ubuntu0.22.04.1 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046499.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046499.html)
- evince 42.3-0ubuntu3.2 - [https://lists.ubuntu.com/archives/jammy-changes/2026-May/046501.html](https://lists.ubuntu.com/archives/jammy-changes/2026-May/046501.html)

End of Standard Support: April 2027

### 

- linux-restricted-signatures 6.8.0-117.117+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055850.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055850.html)
- linux-restricted-modules 6.8.0-117.117+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055851.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055851.html)
- linux-restricted-signatures-hwe-6.17 6.17.0-29.29\~24.04.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055852.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055852.html)
- linux-restricted-modules-hwe-6.17 6.17.0-29.29\~24.04.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055853.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055853.html)
- linux-restricted-signatures-lowlatency 6.8.0-117.117.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055854.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055854.html)
- linux-restricted-modules-lowlatency 6.8.0-117.117.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055855.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055855.html)
- linux-restricted-modules-aws 6.8.0-1055.58+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055856.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055856.html)
- linux-restricted-signatures-aws 6.8.0-1055.58+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055857.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055857.html)
- linux-restricted-signatures-aws-6.17 6.17.0-1015.15\~24.04.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055858.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055858.html)
- linux-restricted-signatures-azure 6.8.0-1054.60+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055859.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055859.html)
- linux-restricted-modules-azure 6.8.0-1054.60+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055860.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055860.html)
- linux-restricted-modules-aws-6.17 6.17.0-1015.15\~24.04.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055861.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055861.html)
- fabric-manager-535 535.309.01-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055862.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055862.html)
- linux-restricted-signatures-azure-6.17 6.17.0-1013.13\~24.04.1+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055863.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055863.html)
- linux-restricted-modules-azure-6.17 6.17.0-1013.13\~24.04.1+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055864.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055864.html)
- fabric-manager-580 580.159.03-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055865.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055865.html)
- linux-restricted-signatures-azure-fde-6.17 6.17.0-1010.10\~24.04.1+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055866.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055866.html)
- linux-restricted-modules-azure-fde-6.17 6.17.0-1010.10\~24.04.1+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055867.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055867.html)
- fabric-manager-595 595.71.05-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055868.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055868.html)
- libnvidia-nscq-535 535.309.01-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055869.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055869.html)
- linux-restricted-signatures-azure-fde 6.8.0-1053.60+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055870.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055870.html)
- linux-restricted-modules-azure-fde 6.8.0-1053.60+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055871.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055871.html)
- libnvidia-nscq-580 580.159.03-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055872.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055872.html)
- linux-restricted-modules-azure-nvidia 6.8.0-1029.32+4 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055873.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055873.html)
- libnvidia-nscq-595 595.71.05-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055874.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055874.html)
- linux-restricted-signatures-azure-nvidia-6.14 6.14.0-1007.7+5 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055875.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055875.html)
- linux-restricted-signatures-azure-nvidia 6.8.0-1029.32+4 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055876.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055876.html)
- linux-restricted-modules-azure-nvidia-6.14 6.14.0-1007.7+5 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055877.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055877.html)
- nvidia-imex-580 580.159.03-0ubuntu0.24.04.2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055878.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055878.html)
- nvidia-imex-595 595.71.05-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055879.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055879.html)
- linux-restricted-signatures-gcp 6.8.0-1058.61+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055880.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055880.html)
- linux-restricted-modules-gcp 6.8.0-1058.61+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055881.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055881.html)
- linux-restricted-signatures-gcp-6.17 6.17.0-1016.17\~24.04.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055882.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055882.html)
- nvidia-graphics-drivers-535 535.309.01-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055883.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055883.html)
- linux-restricted-modules-gcp-6.17 6.17.0-1016.17\~24.04.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055884.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055884.html)
- nvidia-graphics-drivers-580 580.159.03-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055885.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055885.html)
- linux-restricted-signatures-ibm 6.8.0-1055.56+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055887.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055887.html)
- linux-restricted-modules-ibm 6.8.0-1055.56+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055886.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055886.html)
- linux-restricted-modules-oem-6.17 6.17.0-1023.23+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055888.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055888.html)
- linux-restricted-signatures-oem-6.17 6.17.0-1023.23+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055889.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055889.html)
- nvidia-graphics-drivers-535-server 535.309.01-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055890.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055890.html)
- nvidia-graphics-drivers-595 595.71.05-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055891.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055891.html)
- nvidia-graphics-drivers-580-server 580.159.03-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055892.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055892.html)
- linux-restricted-signatures-oracle 6.8.0-1052.53+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055893.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055893.html)
- nvidia-graphics-drivers-595-server 595.71.05-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055894.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055894.html)
- linux-restricted-modules-oracle 6.8.0-1052.53+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055895.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055895.html)
- linux-restricted-modules-oracle-6.17 6.17.0-1014.14\~24.04.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055896.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055896.html)
- linux-restricted-signatures-oracle-6.17 6.17.0-1014.14\~24.04.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055897.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055897.html)
- linux-restricted-modules-nvidia 6.8.0-1054.57+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055898.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055898.html)
- linux-restricted-signatures-nvidia 6.8.0-1054.57+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055899.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055899.html)
- linux-restricted-signatures-nvidia-6.14 6.14.0-1015.15+4 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055900.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055900.html)
- linux-restricted-modules-nvidia-6.14 6.14.0-1015.15+4 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055901.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055901.html)
- linux-restricted-signatures-nvidia-6.17 6.17.0-1018.18+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055902.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055902.html)
- linux-restricted-modules-nvidia-6.17 6.17.0-1018.18+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055903.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055903.html)
- linux-restricted-signatures-nvidia-lowlatency 6.8.0-1054.57.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055904.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055904.html)
- linux-restricted-modules-nvidia-lowlatency 6.8.0-1054.57.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055905.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055905.html)
- linux-restricted-signatures-nvidia-tegra 6.8.0-1023.23+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055906.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055906.html)
- linux-restricted-modules-nvidia-tegra 6.8.0-1023.23+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055907.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055907.html)
- linux-meta-nvidia-6.17 6.17.0-1018.18 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055908.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055908.html)
- linux-signed-nvidia-6.17 6.17.0-1018.18 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055909.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055909.html)
- linux-restricted-signatures-nvidia-6.17 6.17.0-1018.18+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055910.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055910.html)
- linux-restricted-signatures-nvidia-6.17 6.17.0-1018.18+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056021.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056021.html)
- linux-restricted-modules-nvidia-6.17 6.17.0-1018.18+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055911.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055911.html)
- linux-restricted-modules-nvidia-6.17 6.17.0-1018.18+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056023.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056023.html)
- linux-nvidia-6.17 6.17.0-1018.18 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055912.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055912.html)
- linux-restricted-signatures-nvidia-6.17 6.17.0-1018.18 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055913.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055913.html)
- linux-restricted-modules-nvidia-6.17 6.17.0-1018.18 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055914.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055914.html)
- linux-meta 6.8.0-117.117 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055915.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055915.html)
- linux 6.8.0-117.117 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055916.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055916.html)
- linux-signed 6.8.0-117.117 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055917.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055917.html)
- linux-restricted-signatures 6.8.0-117.117 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055918.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055918.html)
- linux-restricted-modules 6.8.0-117.117 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055919.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055919.html)
- linux-meta-aws 6.8.0-1055.58 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055920.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055920.html)
- linux-signed-aws 6.8.0-1055.58 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055921.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055921.html)
- linux-aws 6.8.0-1055.58 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055922.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055922.html)
- linux-restricted-signatures-aws 6.8.0-1055.58 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055923.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055923.html)
- linux-restricted-modules-aws 6.8.0-1055.58 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055924.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055924.html)
- linux-meta-gcp 6.8.0-1058.61 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055925.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055925.html)
- linux-signed-gcp 6.8.0-1058.61 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055926.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055926.html)
- linux-gcp 6.8.0-1058.61 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055927.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055927.html)
- linux-restricted-signatures-gcp 6.8.0-1058.61 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055928.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055928.html)
- linux-restricted-modules-gcp 6.8.0-1058.61 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055929.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055929.html)
- linux-meta-gke 6.8.0-1054.60 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055930.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055930.html)
- linux-signed-gke 6.8.0-1054.60 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055931.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055931.html)
- linux-gke 6.8.0-1054.60 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055932.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055932.html)
- linux-meta-gkeop 6.8.0-1041.44 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055933.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055933.html)
- linux-signed-gkeop 6.8.0-1041.44 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055934.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055934.html)
- linux-meta-ibm 6.8.0-1055.56 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055935.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055935.html)
- linux-gkeop 6.8.0-1041.44 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055938.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055938.html)
- linux-signed-ibm 6.8.0-1055.56 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055936.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055936.html)
- linux-ibm 6.8.0-1055.56 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055937.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055937.html)
- linux-restricted-signatures-ibm 6.8.0-1055.56 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055939.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055939.html)
- linux-restricted-modules-ibm 6.8.0-1055.56 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055940.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055940.html)
- linux-lowlatency 6.8.0-117.117.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055941.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055941.html)
- linux-meta-lowlatency 6.8.0-117.117.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055942.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055942.html)
- linux-signed-lowlatency 6.8.0-117.117.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055943.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055943.html)
- linux-restricted-modules-lowlatency 6.8.0-117.117.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055944.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055944.html)
- linux-restricted-signatures-lowlatency 6.8.0-117.117.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055945.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055945.html)
- linux-meta-nvidia 6.8.0-1054.57 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055946.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055946.html)
- linux-nvidia 6.8.0-1054.57 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055947.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055947.html)
- linux-signed-nvidia 6.8.0-1054.57 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055948.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055948.html)
- linux-restricted-signatures-nvidia 6.8.0-1054.57 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055949.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055949.html)
- linux-restricted-modules-nvidia 6.8.0-1054.57 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055950.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055950.html)
- linux-raspi 6.8.0-1056.60 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055951.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055951.html)
- linux-meta-raspi 6.8.0-1056.60 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055952.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055952.html)
- linux-hwe-6.17 6.17.0-29.29\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055953.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055953.html)
- linux-meta-hwe-6.17 6.17.0-29.29\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055954.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055954.html)
- linux-signed-hwe-6.17 6.17.0-29.29\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055955.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055955.html)
- linux-restricted-modules-hwe-6.17 6.17.0-29.29\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055956.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055956.html)
- linux-restricted-signatures-hwe-6.17 6.17.0-29.29\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055957.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055957.html)
- linux-meta-nvidia-lowlatency 6.8.0-1054.57.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055958.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055958.html)
- linux-signed-nvidia-lowlatency 6.8.0-1054.57.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055959.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055959.html)
- linux-restricted-signatures-nvidia-lowlatency 6.8.0-1054.57.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055960.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055960.html)
- linux-restricted-modules-nvidia-lowlatency 6.8.0-1054.57.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055961.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055961.html)
- linux-nvidia-lowlatency 6.8.0-1054.57.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055962.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055962.html)
- linux-signed-oracle-6.17 6.17.0-1014.14\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055963.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055963.html)
- linux-meta-oracle-6.17 6.17.0-1014.14\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055964.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055964.html)
- linux-oracle-6.17 6.17.0-1014.14\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055965.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055965.html)
- linux-restricted-signatures-oracle-6.17 6.17.0-1014.14\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055966.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055966.html)
- linux-meta-riscv-6.17 6.17.0-29.29.1\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055967.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055967.html)
- linux-restricted-modules-oracle-6.17 6.17.0-1014.14\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055968.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055968.html)
- linux-riscv-6.17 6.17.0-29.29.1\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055969.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055969.html)
- linux-meta-oem-6.17 6.17.0-1023.23 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055970.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055970.html)
- linux-signed-oem-6.17 6.17.0-1023.23 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055971.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055971.html)
- linux-oem-6.17 6.17.0-1023.23 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055972.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055972.html)
- linux-restricted-signatures-oem-6.17 6.17.0-1023.23 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055973.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055973.html)
- linux-restricted-modules-oem-6.17 6.17.0-1023.23 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055974.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055974.html)
- lintian 2.117.0ubuntu1.5 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055975.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055975.html)
- linux-restricted-signatures 6.8.0-117.117+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055976.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055976.html)
- linux-restricted-modules 6.8.0-117.117+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055977.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055977.html)
- linux-restricted-signatures-hwe-6.17 6.17.0-29.29\~24.04.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055978.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055978.html)
- linux-restricted-modules-hwe-6.17 6.17.0-29.29\~24.04.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055979.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055979.html)
- fabric-manager-535 535.309.01-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055980.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055980.html)
- linux-restricted-signatures-lowlatency 6.8.0-117.117.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055981.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055981.html)
- linux-restricted-modules-lowlatency 6.8.0-117.117.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055982.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055982.html)
- linux-restricted-signatures-aws 6.8.0-1055.58+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055983.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055983.html)
- fabric-manager-570 570.211.01-0ubuntu1.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055984.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055984.html)
- linux-restricted-modules-azure 6.8.0-1054.60+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055985.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055985.html)
- fabric-manager-580 580.159.03-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055986.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055986.html)
- linux-restricted-signatures-azure 6.8.0-1054.60+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055987.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055987.html)
- linux-restricted-signatures-azure-6.17 6.17.0-1013.13\~24.04.1+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055988.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055988.html)
- fabric-manager-590 590.48.01-0ubuntu0.24.04.2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055989.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055989.html)
- linux-restricted-modules-azure-nvidia 6.8.0-1029.32+4 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055990.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055990.html)
- linux-restricted-signatures-azure-nvidia 6.8.0-1029.32+4 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055991.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055991.html)
- fabric-manager-595 595.71.05-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055992.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055992.html)
- linux-restricted-modules-aws 6.8.0-1055.58+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055993.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055993.html)
- linux-restricted-modules-azure-nvidia-6.14 6.14.0-1007.7+5 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055994.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055994.html)
- linux-restricted-signatures-azure-nvidia-6.14 6.14.0-1007.7+5 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055995.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055995.html)
- libnvidia-nscq-535 535.309.01-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055996.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055996.html)
- linux-restricted-modules-azure-6.17 6.17.0-1013.13\~24.04.1+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055997.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055997.html)
- libnvidia-nscq-570 570.211.01-0ubuntu1.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055998.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055998.html)
- linux-restricted-signatures-gcp 6.8.0-1058.61+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/055999.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/055999.html)
- linux-restricted-modules-gcp 6.8.0-1058.61+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056000.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056000.html)
- libnvidia-nscq-580 580.159.03-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056001.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056001.html)
- libnvidia-nscq-590 590.48.01-0ubuntu0.24.04.2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056002.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056002.html)
- linux-restricted-signatures-ibm 6.8.0-1055.56+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056005.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056005.html)
- libnvidia-nscq-595 595.71.05-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056003.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056003.html)
- linux-restricted-modules-ibm 6.8.0-1055.56+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056004.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056004.html)
- nvidia-imex-570 570.211.01-0ubuntu1.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056006.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056006.html)
- linux-restricted-modules-oem-6.17 6.17.0-1023.23+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056007.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056007.html)
- linux-restricted-signatures-oem-6.17 6.17.0-1023.23+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056008.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056008.html)
- nvidia-imex-580 580.159.03-0ubuntu0.24.04.2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056009.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056009.html)
- linux-restricted-signatures-oracle-6.17 6.17.0-1014.14\~24.04.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056010.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056010.html)
- nvidia-imex-590 590.48.01-0ubuntu0.24.04.2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056011.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056011.html)
- nvidia-imex-595 595.71.05-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056012.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056012.html)
- linux-restricted-modules-oracle-6.17 6.17.0-1014.14\~24.04.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056013.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056013.html)
- linux-restricted-signatures-nvidia 6.8.0-1054.57+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056014.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056014.html)
- nvidia-graphics-drivers-535 535.309.01-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056015.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056015.html)
- linux-restricted-modules-nvidia 6.8.0-1054.57+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056016.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056016.html)
- linux-restricted-signatures-nvidia-6.14 6.14.0-1015.15+4 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056017.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056017.html)
- nvidia-graphics-drivers-580 580.159.03-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056018.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056018.html)
- linux-restricted-modules-nvidia-6.14 6.14.0-1015.15+4 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056019.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056019.html)
- nvidia-graphics-drivers-595 595.71.05-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056020.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056020.html)
- nvidia-graphics-drivers-535-server 535.309.01-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056022.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056022.html)
- linux-restricted-signatures-nvidia-lowlatency 6.8.0-1054.57.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056024.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056024.html)
- nvidia-graphics-drivers-580-server 580.159.03-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056025.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056025.html)
- linux-restricted-modules-nvidia-lowlatency 6.8.0-1054.57.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056026.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056026.html)
- linux-restricted-signatures-nvidia-tegra 6.8.0-1023.23+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056027.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056027.html)
- linux-restricted-modules-nvidia-tegra 6.8.0-1023.23+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056028.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056028.html)
- nvidia-graphics-drivers-595-server 595.71.05-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056029.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056029.html)
- nvidia-graphics-drivers-570-server 570.211.01-0ubuntu1.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056030.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056030.html)
- nvidia-graphics-drivers-590 590.48.01-0ubuntu0.24.04.5 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056031.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056031.html)
- nvidia-graphics-drivers-590-server 590.48.01-0ubuntu0.24.04.5 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056032.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056032.html)
- nvidia-graphics-drivers-570 570.211.01-0ubuntu1.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056033.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056033.html)
- unbound 1.19.2-1ubuntu3.8 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056034.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056034.html)
- rsync 3.2.7-1ubuntu1.4 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056035.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056035.html)
- gnutls28 3.8.3-1.1ubuntu3.6 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056036.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056036.html)
- openvpn 2.6.19-0ubuntu0.24.04.2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056038.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056038.html)
- xdg-desktop-portal 1.18.4-1ubuntu2.24.04.2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056042.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056042.html)
- google-compute-engine-oslogin 20260116.00-0ubuntu1\~24.04.0 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056044.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056044.html)
- google-osconfig-agent 20251028.00-0ubuntu2\~24.04.0 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056045.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056045.html)
- gce-compute-image-packages 20260116.00-0ubuntu1\~24.04.0 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056046.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056046.html)
- linux-restricted-signatures-hwe-7.0 7.0.0-14.14\~24.04.3+3 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056047.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056047.html)
- linux-restricted-modules-hwe-7.0 7.0.0-14.14\~24.04.3+3 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056048.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056048.html)
- linux-restricted-signatures-nvidia-tegra 6.8.0-1024.24+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056049.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056049.html)
- linux-restricted-modules-nvidia-tegra 6.8.0-1024.24+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056050.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056050.html)
- linux-restricted-signatures-nvidia-bos-7.0 7.0.0-2005.5\~24.04.1+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056051.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056051.html)
- linux-restricted-modules-nvidia-bos-7.0 7.0.0-2005.5\~24.04.1+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056052.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056052.html)
- linux-restricted-signatures-nvidia-7.0 7.0.0-1006.6\~24.04.1+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056053.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056053.html)
- linux-restricted-modules-nvidia-7.0 7.0.0-1006.6\~24.04.1+2 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056054.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056054.html)
- snapd 2.75.2+ubuntu24.04 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056055.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056055.html)
- libarchive 3.7.2-2ubuntu0.7 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056056.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056056.html)
- linux-meta-nvidia-tegra 6.8.0-1024.24 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056057.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056057.html)
- linux-signed-nvidia-tegra 6.8.0-1024.24 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056058.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056058.html)
- linux-restricted-modules-nvidia-tegra 6.8.0-1024.24+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056059.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056059.html)
- linux-restricted-signatures-nvidia-tegra 6.8.0-1024.24+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056060.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056060.html)
- linux-nvidia-tegra-modules 6.8.0-1024.24 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056062.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056062.html)
- linux-main-modules-nvidia-tegra 6.8.0-1024.24 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056061.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056061.html)
- linux-nvidia-tegra-modules-signed 6.8.0-1024.24 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056063.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056063.html)
- linux-main-signed-nvidia-tegra 6.8.0-1024.24 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056064.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056064.html)
- linux-meta-azure 6.8.0-1056.62 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056065.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056065.html)
- linux-signed-azure 6.8.0-1056.62 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056066.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056066.html)
- linux-restricted-modules-azure 6.8.0-1056.62+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056067.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056067.html)
- linux-restricted-signatures-azure 6.8.0-1056.62+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056068.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056068.html)
- linux-nvidia-tegra 6.8.0-1024.24 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056069.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056069.html)
- linux-meta-azure-6.17 6.17.0-1015.15\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056070.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056070.html)
- linux-signed-azure-6.17 6.17.0-1015.15\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056071.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056071.html)
- linux-restricted-modules-azure-6.17 6.17.0-1015.15\~24.04.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056072.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056072.html)
- linux-restricted-signatures-azure-6.17 6.17.0-1015.15\~24.04.1+1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056073.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056073.html)
- linux-azure-6.17 6.17.0-1015.15\~24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056074.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056074.html)
- linux-azure 6.8.0-1056.62 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056075.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056075.html)
- libarchive 3.7.2-2ubuntu0.7 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056076.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056076.html)
- bind9 1:9.18.39-0ubuntu0.24.04.5 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056077.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056077.html)
- postgresql-16 16.14-0ubuntu0.24.04.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056079.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056079.html)
- evince 46.3.1-0ubuntu1.1 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056081.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056081.html)
- alsa-ucm-conf 1.2.10-1ubuntu5.11 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056082.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056082.html)
- apparmor 4.0.1really4.0.1-0ubuntu0.24.04.7 - [https://lists.ubuntu.com/archives/noble-changes/2026-May/056084.html](https://lists.ubuntu.com/archives/noble-changes/2026-May/056084.html)

End of standard support: April 2029

### 

- linux-restricted-signatures 6.17.0-29.29+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011877.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011877.html)
- linux-restricted-signatures-aws 6.17.0-1015.15+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011878.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011878.html)
- linux-restricted-modules-aws 6.17.0-1015.15+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011879.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011879.html)
- linux-restricted-modules 6.17.0-29.29+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011880.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011880.html)
- linux-restricted-signatures-azure 6.17.0-1013.13+2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011881.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011881.html)
- linux-restricted-modules-azure 6.17.0-1013.13+2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011882.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011882.html)
- linux-restricted-signatures-azure-fde 6.17.0-1010.10+2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011883.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011883.html)
- linux-restricted-modules-azure-fde 6.17.0-1010.10+2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011884.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011884.html)
- linux-restricted-signatures-gcp 6.17.0-1016.17+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011885.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011885.html)
- linux-restricted-modules-gcp 6.17.0-1016.17+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011886.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011886.html)
- linux-restricted-signatures-oracle 6.17.0-1014.14+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011887.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011887.html)
- linux-restricted-modules-oracle 6.17.0-1014.14+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011888.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011888.html)
- fabric-manager-580 580.159.03-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011889.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011889.html)
- fabric-manager-595 595.71.05-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011890.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011890.html)
- libnvidia-nscq-595 595.71.05-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011891.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011891.html)
- libnvidia-nscq-580 580.159.03-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011892.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011892.html)
- nvidia-imex-580 580.159.03-0ubuntu0.25.10.2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011893.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011893.html)
- nvidia-imex-595 595.71.05-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011894.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011894.html)
- nvidia-graphics-drivers-580 580.159.03-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011895.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011895.html)
- nvidia-graphics-drivers-595 595.71.05-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011896.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011896.html)
- nvidia-graphics-drivers-580-server 580.159.03-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011897.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011897.html)
- nvidia-graphics-drivers-595-server 595.71.05-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011898.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011898.html)
- linux 6.17.0-29.29 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011899.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011899.html)
- linux-meta 6.17.0-29.29 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011900.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011900.html)
- linux-signed 6.17.0-29.29 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011901.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011901.html)
- linux-restricted-modules 6.17.0-29.29 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011902.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011902.html)
- linux-restricted-signatures 6.17.0-29.29 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011903.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011903.html)
- linux-meta-aws 6.17.0-1015.15 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011905.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011905.html)
- linux-aws 6.17.0-1015.15 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011904.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011904.html)
- linux-signed-aws 6.17.0-1015.15 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011906.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011906.html)
- linux-restricted-signatures-aws 6.17.0-1015.15 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011907.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011907.html)
- linux-meta-oracle 6.17.0-1014.14 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011908.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011908.html)
- linux-restricted-modules-aws 6.17.0-1015.15 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011909.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011909.html)
- linux-oracle 6.17.0-1014.14 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011910.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011910.html)
- linux-signed-oracle 6.17.0-1014.14 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011911.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011911.html)
- linux-restricted-signatures-oracle 6.17.0-1014.14 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011912.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011912.html)
- linux-meta-raspi 6.17.0-1017.17 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011913.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011913.html)
- linux-restricted-modules-oracle 6.17.0-1014.14 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011915.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011915.html)
- linux-raspi 6.17.0-1017.17 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011914.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011914.html)
- linux-meta-realtime 6.17.0-1013.15 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011916.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011916.html)
- linux-signed-realtime 6.17.0-1013.15 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011917.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011917.html)
- linux-realtime 6.17.0-1013.15 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011918.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011918.html)
- linux-meta-riscv 6.17.0-29.29.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011919.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011919.html)
- linux-riscv 6.17.0-29.29.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011920.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011920.html)
- lintian 2.122.0ubuntu2.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011921.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011921.html)
- linux-restricted-signatures 6.17.0-29.29+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011922.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011922.html)
- linux-restricted-signatures-aws 6.17.0-1015.15+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011923.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011923.html)
- linux-restricted-modules 6.17.0-29.29+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011924.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011924.html)
- linux-restricted-modules-aws 6.17.0-1015.15+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011925.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011925.html)
- linux-restricted-signatures-azure 6.17.0-1013.13+2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011926.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011926.html)
- linux-restricted-modules-azure 6.17.0-1013.13+2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011927.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011927.html)
- linux-restricted-signatures-oracle 6.17.0-1014.14+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011928.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011928.html)
- linux-restricted-modules-oracle 6.17.0-1014.14+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011929.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011929.html)
- fabric-manager-580 580.159.03-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011930.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011930.html)
- fabric-manager-590 590.48.01-0ubuntu0.25.10.2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011931.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011931.html)
- fabric-manager-595 595.71.05-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011932.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011932.html)
- libnvidia-nscq-580 580.159.03-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011933.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011933.html)
- libnvidia-nscq-590 590.48.01-0ubuntu0.25.10.2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011934.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011934.html)
- libnvidia-nscq-595 595.71.05-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011935.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011935.html)
- nvidia-imex-580 580.159.03-0ubuntu0.25.10.2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011936.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011936.html)
- nvidia-imex-590 590.48.01-0ubuntu0.25.10.2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011937.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011937.html)
- nvidia-imex-595 595.71.05-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011938.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011938.html)
- nvidia-graphics-drivers-580 580.159.03-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011939.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011939.html)
- nvidia-graphics-drivers-595 595.71.05-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011940.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011940.html)
- nvidia-graphics-drivers-580-server 580.159.03-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011941.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011941.html)
- nvidia-graphics-drivers-595-server 595.71.05-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011942.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011942.html)
- nvidia-graphics-drivers-590 590.48.01-0ubuntu0.25.10.5 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011943.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011943.html)
- nvidia-graphics-drivers-590-server 590.48.01-0ubuntu0.25.10.5 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011944.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011944.html)
- unbound 1.22.0-2ubuntu2.3 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011945.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011945.html)
- rsync 3.4.1+ds1-5ubuntu1.2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011946.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011946.html)
- gnutls28 3.8.9-3ubuntu2.2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011947.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011947.html)
- gst-plugins-good1.0 1.26.5-1ubuntu2.2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011948.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011948.html)
- unbound 1.22.0-2ubuntu2.3 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011949.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011949.html)
- openvpn 2.6.19-0ubuntu0.25.10.2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011950.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011950.html)
- gst-plugins-good1.0 1.26.5-1ubuntu2.2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011953.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011953.html)
- xdg-desktop-portal 1.20.3+ds-1ubuntu1.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011955.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011955.html)
- bubblewrap 0.11.0-2ubuntu0.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011956.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011956.html)
- google-compute-engine-oslogin 20260116.00-0ubuntu1\~25.10.0 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011959.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011959.html)
- google-osconfig-agent 20251028.00-0ubuntu2\~25.10.0 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011960.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011960.html)
- gce-compute-image-packages 20260116.00-0ubuntu1\~25.10.0 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011961.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011961.html)
- snapd 2.75.2+ubuntu25.10 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011962.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011962.html)
- libarchive 3.7.7-0ubuntu3.2 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011963.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011963.html)
- linux-meta-azure 6.17.0-1015.15 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011964.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011964.html)
- linux-signed-azure 6.17.0-1015.15 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011965.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011965.html)
- linux-restricted-signatures-azure 6.17.0-1015.15+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011966.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011966.html)
- linux-restricted-modules-azure 6.17.0-1015.15+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011967.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011967.html)
- linux-azure 6.17.0-1015.15 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011968.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011968.html)
- linux-meta-azure-fde 6.17.0-1012.12 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011969.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011969.html)
- linux-signed-azure-fde 6.17.0-1012.12 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011970.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011970.html)
- linux-restricted-modules-azure-fde 6.17.0-1012.12+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011971.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011971.html)
- linux-restricted-signatures-azure-fde 6.17.0-1012.12+1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011972.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011972.html)
- linux-azure-fde 6.17.0-1012.12 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011973.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011973.html)
- bind9 1:9.20.11-1ubuntu2.4 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011975.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011975.html)
- postgresql-17 17.10-0ubuntu0.25.10.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011977.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011977.html)
- evince 48.1-3ubuntu2.1 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011979.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011979.html)
- alsa-ucm-conf 1.2.12-1ubuntu2.4 - [https://lists.ubuntu.com/archives/questing-changes/2026-May/011980.html](https://lists.ubuntu.com/archives/questing-changes/2026-May/011980.html)

End of Life: July 2026

### 

- linux-restricted-signatures 7.0.0-15.15+2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027576.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027576.html)
- linux-restricted-signatures-aws 7.0.0-1004.4+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027577.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027577.html)
- linux-restricted-modules 7.0.0-15.15+2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027578.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027578.html)
- linux-restricted-modules-aws 7.0.0-1004.4+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027579.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027579.html)
- linux-restricted-signatures-azure 7.0.0-1004.4+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027580.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027580.html)
- linux-restricted-modules-azure 7.0.0-1004.4+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027581.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027581.html)
- linux-restricted-signatures-azure-fde 7.0.0-1004.4+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027582.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027582.html)
- linux-restricted-modules-azure-fde 7.0.0-1004.4+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027583.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027583.html)
- linux-restricted-signatures-gcp 7.0.0-1003.3+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027584.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027584.html)
- linux-restricted-modules-gcp 7.0.0-1003.3+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027585.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027585.html)
- linux-restricted-signatures-ibm 7.0.0-1005.5+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027586.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027586.html)
- linux-restricted-modules-ibm 7.0.0-1005.5+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027587.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027587.html)
- linux-restricted-modules-oracle 7.0.0-1003.3+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027588.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027588.html)
- linux-restricted-signatures-oracle 7.0.0-1003.3+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027589.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027589.html)
- linux-restricted-signatures-nvidia 7.0.0-1006.6+2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027590.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027590.html)
- linux-restricted-modules-nvidia 7.0.0-1006.6+2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027591.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027591.html)
- nvidia-graphics-drivers-580 580.159.03-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027592.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027592.html)
- nvidia-graphics-drivers-595 595.71.05-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027593.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027593.html)
- nvidia-graphics-drivers-580-server 580.159.03-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027594.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027594.html)
- nvidia-graphics-drivers-595-server 595.71.05-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027595.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027595.html)
- accountsservice 23.13.9-8ubuntu5.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027596.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027596.html)
- gnome-session 50.0-0ubuntu3.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027597.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027597.html)
- gnome-sushi 50.0-0ubuntu0.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027598.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027598.html)
- lintian 2.129.0ubuntu2.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027599.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027599.html)
- linux-restricted-signatures-aws 7.0.0-1004.4+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027600.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027600.html)
- linux-restricted-modules-aws 7.0.0-1004.4+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027601.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027601.html)
- linux-restricted-signatures-azure 7.0.0-1004.4+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027602.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027602.html)
- linux-restricted-modules-azure 7.0.0-1004.4+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027603.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027603.html)
- linux-restricted-signatures-azure-fde 7.0.0-1004.4+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027604.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027604.html)
- linux-restricted-modules-azure-fde 7.0.0-1004.4+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027605.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027605.html)
- linux-restricted-signatures-gcp 7.0.0-1003.3+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027606.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027606.html)
- linux-restricted-modules-gcp 7.0.0-1003.3+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027607.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027607.html)
- linux-restricted-modules-ibm 7.0.0-1005.5+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027608.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027608.html)
- linux-restricted-signatures-ibm 7.0.0-1005.5+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027609.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027609.html)
- linux-restricted-signatures-oracle 7.0.0-1003.3+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027610.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027610.html)
- linux-restricted-modules-oracle 7.0.0-1003.3+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027611.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027611.html)
- linux-restricted-signatures-nvidia 7.0.0-1006.6+2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027612.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027612.html)
- linux-restricted-modules-nvidia 7.0.0-1006.6+2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027613.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027613.html)
- nvidia-graphics-drivers-580 580.159.03-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027614.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027614.html)
- nvidia-graphics-drivers-595 595.71.05-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027615.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027615.html)
- nvidia-graphics-drivers-580-server 580.159.03-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027616.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027616.html)
- nvidia-graphics-drivers-595-server 595.71.05-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027617.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027617.html)
- linux-signed 7.0.0-15.15 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027618.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027618.html)
- linux 7.0.0-15.15 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027619.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027619.html)
- linux-restricted-signatures 7.0.0-15.15+2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027620.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027620.html)
- linux-meta 7.0.0-15.15 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027621.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027621.html)
- linux-main-signed 7.0.0-15.15+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027622.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027622.html)
- linux-main-modules 7.0.0-15.15+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027623.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027623.html)
- linux-restricted-modules 7.0.0-15.15+2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027624.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027624.html)
- unbound 1.24.2-1ubuntu2.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027625.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027625.html)
- rsync 3.4.1+ds1-7ubuntu0.2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027626.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027626.html)
- gnutls28 3.8.12-2ubuntu1.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027627.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027627.html)
- openvpn 2.7.0-1ubuntu1.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027629.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027629.html)
- bubblewrap 0.11.1-1ubuntu0.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027633.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027633.html)
- kquickimageeditor 0.6.0-2ubuntu0.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027635.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027635.html)
- cinnamon 6.4.13-2ubuntu0.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027636.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027636.html)
- linux-firmware-raspi 14-0ubuntu1.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027637.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027637.html)
- linux-restricted-signatures-nvidia-bos 7.0.0-2005.5+2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027638.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027638.html)
- linux-restricted-modules-nvidia-bos 7.0.0-2005.5+2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027639.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027639.html)
- linux-restricted-signatures 7.0.0-17.17+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027640.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027640.html)
- linux-restricted-modules 7.0.0-17.17+1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027641.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027641.html)
- kf6-kguiaddons 6.24.0-0ubuntu1.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027642.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027642.html)
- gnome-control-center 1:50.0-0ubuntu6.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027643.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027643.html)
- snapd 2.75.2+ubuntu26.04.2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027644.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027644.html)
- libarchive 3.8.5-1ubuntu2.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027645.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027645.html)
- bind9 1:9.20.18-1ubuntu2.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027647.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027647.html)
- postgresql-18 18.4-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027649.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027649.html)
- fabric-manager-580 580.159.03-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027651.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027651.html)
- fabric-manager-595 595.71.05-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027652.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027652.html)
- libnvidia-nscq-580 580.159.03-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027653.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027653.html)
- libnvidia-nscq-595 595.71.05-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027654.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027654.html)
- nvidia-imex-580 580.159.03-0ubuntu0.26.04.2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027655.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027655.html)
- nvidia-imex-595 595.71.05-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027656.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027656.html)
- fabric-manager-580 580.159.03-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027658.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027658.html)
- fabric-manager-595 595.71.05-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027657.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027657.html)
- libnvidia-nscq-580 580.159.03-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027659.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027659.html)
- libnvidia-nscq-595 595.71.05-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027660.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027660.html)
- nvidia-imex-580 580.159.03-0ubuntu0.26.04.2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027661.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027661.html)
- nvidia-imex-595 595.71.05-0ubuntu0.26.04.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027662.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027662.html)
- evince 49\~alpha-2ubuntu2.1 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027663.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027663.html)
- alsa-ucm-conf 1.2.15.3-1ubuntu1.2 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027664.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027664.html)
- ubuntu-release-upgrader 1:26.04.21 - [https://lists.ubuntu.com/archives/resolute-changes/2026-May/027666.html](https://lists.ubuntu.com/archives/resolute-changes/2026-May/027666.html)

End of Standard Support: April 2031

## 

Get your copy of the Ubuntu Weekly Newsletter delivered each week to you via email at: [https://lists.ubuntu.com/mailman/listinfo/ubuntu-news](https://lists.ubuntu.com/mailman/listinfo/ubuntu-news)

Or follow us via our various social media presences:

- [https://www.facebook.com/UbuntuWeeklyNewsletter](https://www.facebook.com/UbuntuWeeklyNewsletter)
- [https://twitter.com/Ubuntu\_News](https://twitter.com/Ubuntu_News)
- [https://t.me/ubuntunewsletter](https://t.me/ubuntunewsletter) (Telegram)
- [https://discourse.ubuntu.com/c/uwn/uwn-issues/419.rss](https://discourse.ubuntu.com/c/uwn/uwn-issues/419.rss) (our RSS feed)

## 

For recent issues of the Ubuntu Weekly Newsletter [Issue 786 & later please visit our Discourse page:](https://discourse.ubuntu.com/c/uwn/uwn-issues/419) or [our Portal page:](https://ubuntu.com/community/uwn/) that is easier to read. The older WIKI issues (809 and earlier) are available at[: UbuntuWeeklyNewsletter/Archive](https://wiki.ubuntu.com/UbuntuWeeklyNewsletter/Archive).

## 

As always you can find more Ubuntu news and announcements at:

## 

Thank you for reading the Ubuntu Weekly Newsletter.

See you next week!

## 

The Ubuntu Weekly Newsletter is brought to you by:

- Krytarik Raido
- Bashing-om
- Chris Guiver
- Wild Man
- Cristovao Cordeiro (cjdc) - Rocks
- irihapeti
- And many others

## 

Other acronyms can be found at: [https://discourse.ubuntu.com/t/glossary-uwn/42405](https://discourse.ubuntu.com/t/glossary-uwn/42405)

## 

The Ubuntu community consists of individuals and teams, working on different aspects of the distribution, giving advice and technical support, and helping to promote Ubuntu to a wider audience. No contribution is too small, and anyone can help. It’s your chance to get in on all the community fun associated with developing and promoting Ubuntu. More on this at: [https://community.ubuntu.com/contribute/](https://community.ubuntu.com/contribute/)

Or get involved with the Ubuntu Weekly Newsletter team! We always need summary writers and editors, if you’re interested, learn more at: [https://discourse.ubuntu.com/t/joining-the-ubuntu-weekly-newsletter-team/40929](https://discourse.ubuntu.com/t/joining-the-ubuntu-weekly-newsletter-team/40929)

## 

This document is maintained by the Ubuntu Weekly News Team. If you have a story idea or suggestions for the Weekly Newsletter, join the Ubuntu News Team mailing list at [https://lists.ubuntu.com/mailman/listinfo/Ubuntu-news-team](https://lists.ubuntu.com/mailman/listinfo/Ubuntu-news-team) and submit it. Ideas can also be added to the wiki at [https://discourse.ubuntu.com/t/ubuntu-weekly-newsletter-ideas/40053/](https://discourse.ubuntu.com/t/ubuntu-weekly-newsletter-ideas/40053/) . If you’d like to contribute to a future issue of the Ubuntu Weekly Newsletter, please feel free to edit the appropriate wiki page. If you have any technical support questions, please check [https://community.ubuntu.com/help-information/](https://community.ubuntu.com/help-information/) for more information on where to get help.

Except where otherwise noted, this issue of the Ubuntu Weekly Newsletter is licensed under a Creative Commons Attribution ShareAlike 3.0 License.
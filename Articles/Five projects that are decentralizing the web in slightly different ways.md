# Five projects that are decentralizing the web in slightly different ways
## Or, why the Internet will be different this time around
![](https://cdn-images-1.medium.com/max/1600/1*dVMOYGE88Nxkay2U0pOs4g.jpeg)

Time to change our focus a little bit here. On this blog, we’ve talked almost exclusively about IPFS and more general decentralized web concepts. We haven’t really touched on other projects much at all. This mostly because Textile is building on IPFS now. We did a lot of research on current solutions before we decided on IPFS. Building on top of IPFS is helping us quickly develop solutions to a few of those primitives in ways that mobile developers will be able to easily reuse, to build the next 1000 decentralized apps. Also, the project ethos and ideals are in-line with our own, which makes working with the IPFS team a great experience.

But there are other players in the game, some complimentary, some competition, but all of them share the common goal of a better, more open internet for everyone. It really is an exciting time to be developing in this space. So let’s take a quick look at some of these projects, and see how others conceptualize the decentralized web. Note that I’m going to specifically focus on decentralized web examples. So we’re leaving out things like Ethereum (which already has tons and tons of blog posts devoted to it anyway), and more specific Dapps like DTube, etc. Anyway, let’s get started and you’ll see what we’re talking about… here are the TL;DRs:

#### Zeronet
>Open, free and uncensorable websites, using Bitcoin cryptography and BitTorrent network

For the most part, Zeronet is focused on decentralized websites and resisting censorship. The use public key infrastructure to publish (private) and verify (public) site content. To make this as easy as possible, they use your Bitcoin wallet, which means no passwords required. This is a really nice feature of crypto-based projects… and something Zeronet demonstrates to great effect. Data exchange is enabled using BitTorrent trackers, and each site is treated like a single Torrent (which is a very intuitive idea). The project supports Tor to help hide your IP address, which makes connections private (though like IPFS, this is not the default).

The way sites on Zeronet work is that each site has a JSON manifest with references to all the other files that make up a site. Once you visit a given site, you start to ‘seed’ it. The really nice thing about the Zeronet implementation is that it supports dynamic updates through pushes to seeding clients. Another nice feature is that it supports multi-user sites, which is something that is a little bit more tricky on say IPFS. To access the ZeroNet, you’ll need to run their software, which is essentially a local browser-based web-app. Zeronet uses .bit domain names, which is based on a decentralized DNS system using the Namecoin cryptocurrency.

#### MaidSafe
>Provide security and privacy for everyone on the planet

This project is largely focused on censorship, privacy, security, and probably most importantly, control of personal data. In the MaidSafe world (SAFE Network), you ‘pay’ for adding content (creating sites etc), but not browsing or accessing content. They support their own market, driven by a cryptocoin (the Safecoin), which is fully autonomous; so the theory here is it will be self-regulating… The way content works on the SAFE Network is that data/content is distributed across all ‘peers’ in the network, and data storage is automatically decentralized (so you end up indirectly hosting data for others…). Safecoin is the incentive mechanism for seeding content on network, which is similar to idea of Filecoin on IPFS. So in the MaidSafe universe, nodes are called Vaults, and are rewarded with Safecoin for storing and hosting data. This cryptocoin is like a digital cash with no public ledger, so it cannot be used outside of the network. This is actually a really cool idea, and is part of the reason their network is potentially autonomous. The thing here is that it is not based on a blockchain, so payments can be anonymous. To explore the SAFE Network, you’ll need to download and use the SAFE Browser, which acts as secure gateway to the network, and also does things like store passwords, data, apps etc…

Some trivia: apparently MaidSafe was actually part of the inspiration for PiedPiper’s decentralized Internet in the HBO TV show called Silicon Valley… so that’s pretty cool. Finally, the decentralized web has (kinda) hit mainstream.

#### Dat/Hypercore/Beaker
>Dat is a nonprofit-backed data sharing protocol for applications of the future

Dat is the protocol. It is developed by Code for Science & Society, which is a U.S. 501(c)(3) nonprofit, with funding mostly from private foundations. This is a really interesting funding model, and the project admins are super open about their funding and what they do with it. The whole system is quite intuitive, focused on building sustainable protocols and standards, and is very open. The main idea is that content is accessed via public-key-addressed file archives (i.e., zip archives), as opposed to content hashed addresses like in IPFS. Dat automatically tracks version history which is really nice, but, this makes it slightly difficult to share keys between devices, which, because of version tracking, can lead to errors if the history splits… for now.

Hypercore is the storage, content, and networking protocols underlying Dat. Here feeds are the core mechanism used in Dat, which are binary append-only streams whose contents are cryptographically hashed and signed. This is nice, because it builds trust into the system. Beaker browser, which is totally separate project, is a (the!) browser that supports Dat (it also used to support IPFS). The nice thing here is that the Beaker browser does a great job of taking advantage of the underlying Dat protocol and mutability of a public-key based system. Beaker makes it super easy to seed, fork, edit, and publish content, and even supports things like private data sharing, deduplication of content and content history, etc. Basically the relationship between Dat (protocols, low-level) and Beaker (interface, high-level) is similar in concept to the relationship between git and GitHub and/or GitLab.

#### Freenet
>Browse websites, post on forums, and publish files within Freenet with strong privacy protections

Freenet is a peer-to-peer platform focused on activists and people living in repressive regimes. It is the result of many academic papers and developer interactions, has been around for a while, and is very much ideals driven. On the Freenet, interactions are anonymous, you can browse freesites (so it is a separate Internet), chat, interact on forums, etc. All communications are routed through peers similar to a Tor network, and all data is stored across all peers in encrypted format. The devs for the project are very honest about how the network works, and while you cannot easily discover what’s in a particular datastore (that might be stored on your computer), the devs simply state that you “hopefully can’t be held accountable for it”… If these types of issues concern you, you can enable a ‘web of trust’ feature in high security mode, which allows users (you) to be effectively undetectable outside your network of contacts, and also only share/store content with your direct peers. This is a really powerful idea, and is similar to private networks on IPFS.

Some other useful tidbits about Feenet include that is was started by Mike Godwin (see Godwin’s law)from the Electronic Frontier Foundation, and members of the project are actively involved in court cases around censorship resistant communications. As a result, the project has a big focus on advocacy, privacy, rights, etc. In fact, the project is so serious about privacy and Internet safety, that the Freenet software may strip JavaScript, CSS, and other ‘unsafe’ assets from hosted content to protect its users!

#### Blockstack
>The easiest way to start building decentralized blockchain apps

Blockstack is a fully decentralized standalone Internet. The big focus of the project seems to be on data ownership, privacy, security and freedom. It comes with stack of open-source developer tools to build and bootstrap decentralized applications and protocol ecosystems (which is quite nice). It uses a decentralized DNS-like system stored on the Ethereum blockchain (Correction: Blockstack is built on the bitcoin blockchain) to support namespaces. As with many of the other projects listed here, it requires a specialized browser portal. One of the best comparisons I’ve seen for Blockstack is with Firebase. You have a stack of SDKs, a Browser, the Blockstack name service (BNS), plus decentralized storage system, etc… So it is designed to be a full-stack alternative decentralized Internet. In fact, it even has its own ‘Layer-2’ blockchain.

At the moment, the project seems to be quite quite developer-focused, with core features designed to make development on Blockstack relatively easy. They’ve already got some feature Dapps that work and provide a nice demo into the capabilities of the system. Being a one-stop solution, they already have a Blockstack ID for user identity, built-in facilities for storing personal data (decentralized), a development platform with user-friendly APIs, etc. Really, everything you might need to start decentralizing the application layer.

#### Special mention: Tor
>Protect your privacy. Defend yourself against network surveillance and traffic analysis

If you haven’t already heard of Tor, it is an open network of peers designed to defend against traffic analysis. Essentially, peers connect through a series of virtual tunnels, rather than direct connections. These indirect connections help to hide your IP address among other users on network. The more populous and diverse the Tor network, the more anonymous the overall network becomes. It has been around for ages, but with the advent of new and emerging decentralized web solutions, it is getting renewed attention, and for good reason. In fact, many other platforms and protocols are building in support for Tor networks by default, which in turn adds peers to Tor network, which in turn makes the network even more effective!

You can think of Tor as operating at the communication layer, although the project does develop/contribute to browsers and extensions, OS layer integrations, relays, etc. The way it works is that anyone can be a relay (so traffic is routed through your reply), though this requires volunteering, as no (monetary) incentive mechanisms exist.

#### And there you have it
This post has covered just a few of the decentralized web projects we’re keeping on eye on here at Textile. There are plenty of others out there, and plenty more to learn about these individual projects. We encourage you get check them out, play around with what they have to offer, and let us know what you think. Did we miss something critical? Are we misrepresenting the project? What else should we be ready to learn more? If you’re up to it, share your thoughts on Twitter, or tell us what other cool distributed web projects you’re working on — we’d love to hear about it! In the mean time, why not signup for our Textile Photos waitlist to see what else we’re up to…

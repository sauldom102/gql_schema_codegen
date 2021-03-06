from enum import Enum
from typing import ClassVar, List, Optional, TypedDict


AbilitiesEnum = Enum('AbilitiesEnum', 'adaptability aerilate aftermath airlock analytic angerpoint anticipation arenatrap aromaveil asoneasoneglastrier asonespectrier aurabreak baddreams ballfetch battery battlearmor battlebond beastboost berserk bigpecks blaze bulletproof cheekpouch chillingneigh chlorophyll clearbody cloudnine colorchange comatose competitive compoundeyes contrary corrosion cottondown curiousmedicine cursedbody cutecharm damp dancer darkaura dauntlessshield dazzling defeatist defiant deltastream desolateland disguise download dragonsmaw drizzle drought dryskin earlybird effectspore electricsurge emergencyexit fairyaura filter flamebody flareboost flashfire flowergift flowerveil fluffy forecast forewarn friendguard frisk fullmetalbody furcoat galewings galvanize gluttony gooey gorillatactics grasspelt grassysurge grimneigh gulpmissile guts harvest healer heatproof heavymetal honeygather hugepower hungerswitch hustle hydration hypercutter icebody iceface icescales illuminate illusion immunity imposter infiltrator innardsout innerfocus insomnia intimidate intrepidsword ironbarbs ironfist justified keeneye klutz leafguard levitate libero lightmetal lightningrod limber liquidooze liquidvoice longreach magicbounce magicguard magician magmaarmor magnetpull marvelscale megalauncher merciless mimicry minus mirrorarmor mistysurge moldbreaker moody motordrive mountaineer moxie multiscale multitype mummy naturalcure neuroforce noability neutralizinggas noguard normalize oblivious overcoat overgrow owntempo parentalbond persistent pastelveil perishbody pickpocket pickup pixilate plus poisonheal poisonpoint poisontouch powerconstruct powerofalchemy powerspot prankster pressure primordialsea prismarmor propellertail protean psychicsurge punkrock purepower queenlymajesty quickdraw quickfeet rkssystem raindish rattled rebound receiver reckless refrigerate regenerator ripen rivalry rockhead roughskin runaway sandforce sandrush sandspit sandstream sandveil sapsipper schooling scrappy screencleaner serenegrace shadowshield shadowtag shedskin sheerforce shellarmor shielddust shieldsdown simple skilllink slowstart slushrush sniper snowcloak snowwarning solarpower solidrock soulheart soundproof speedboost stakeout stall stalwart stamina stancechange static steadfast steamengine steelworker steelyspirit stench stickyhold stormdrain strongjaw sturdy suctioncups superluck surgesurfer swarm sweetveil swiftswim symbiosis synchronize tangledfeet tanglinghair technician telepathy teravolt thickfat tintedlens torrent toughclaws toxicboost trace transistor triage truant turboblaze unaware unburden unnerve unseenfist victorystar vitalspirit voltabsorb wanderingspirit waterabsorb waterbubble watercompaction waterveil weakarmor whitesmoke wimpout wonderguard wonderskin zenmode')


PokemonEnum = Enum('PokemonEnum', 'syclar syclant revenankh embirch flarelm pyroak breezi fidgit rebble tactite stratagem privatyke arghonaut kitsunoh cyclohm colossoil krilowatt voodoll voodoom scratchet tomohawk necturine necturna mollux cupra argalis aurumoth brattler malaconda cawdet cawmodore volkritter volkraken snugglow plasmanta floatoy caimanoe naviathan crucibelle crucibellemega pluffle kerfluffle pajantom mumbao jumbao fawnifer electrelk caribolt smogecko smoguana smokomodo swirlpool coribalis snaelstrom justyke equilibra solotl astrolotl miasmite miasmaw chromera nohface monohm duohm dorsoil protowatt venomicon venomiconepilogue missingno bulbasaur ivysaur venusaur venusaurgmax venusaurmega charmander charmeleon charizard charizardmegax charizardmegay charizardgmax squirtle wartortle blastoise blastoisegmax blastoisemega caterpie metapod butterfree butterfreegmax weedle kakuna beedrill beedrillmega pidgey pidgeotto pidgeot pidgeotmega rattata rattataalola raticate raticatealola raticatealolatotem spearow fearow ekans arbok pikachu pikachugmax pikachucosplay pikachurockstar pikachubelle pikachupopstar pikachuphd pikachulibre pikachuoriginal pikachuhoenn pikachusinnoh pikachuunova pikachukalos pikachualola pikachupartner pikachustarter pikachuworld raichu raichualola sandshrew sandshrewalola sandslash sandslashalola nidoranf nidorina nidoqueen nidoranm nidorino nidoking clefairy clefable vulpix vulpixalola ninetales ninetalesalola jigglypuff wigglytuff zubat golbat oddish gloom vileplume paras parasect venonat venomoth diglett diglettalola dugtrio dugtrioalola meowth meowthalola meowthgalar meowthgmax persian persianalola psyduck golduck mankey primeape growlithe growlithehisui arcanine arcaninehisui poliwag poliwhirl poliwrath abra kadabra alakazam alakazammega machop machoke machamp machampgmax bellsprout weepinbell victreebel tentacool tentacruel geodude geodudealola graveler graveleralola golem golemalola ponyta ponytagalar rapidash rapidashgalar slowpoke slowpokegalar slowbro slowbrogalar slowbromega magnemite magneton farfetchd farfetchdgalar doduo dodrio seel dewgong grimer grimeralola muk mukalola shellder cloyster gastly haunter gengar gengarmega gengargmax onix drowzee hypno krabby kingler kinglergmax voltorb voltorbhisui electrode electrodehisui exeggcute exeggutor exeggutoralola cubone marowak marowakalola marowakalolatotem hitmonlee hitmonchan lickitung koffing weezing weezinggalar rhyhorn rhydon chansey tangela kangaskhan kangaskhanmega horsea seadra goldeen seaking staryu starmie mrmime mrmimegalar scyther jynx electabuzz magmar pinsir pinsirmega tauros magikarp gyarados gyaradosmega lapras laprasgmax ditto eevee eeveestarter eeveegmax vaporeon jolteon flareon porygon omanyte omastar kabuto kabutops aerodactyl aerodactylmega snorlax snorlaxgmax articuno articunogalar zapdos zapdosgalar moltres moltresgalar dratini dragonair dragonite mewtwo mewtwomegax mewtwomegay mew chikorita bayleef meganium cyndaquil quilava typhlosion typhlosionhisui totodile croconaw feraligatr sentret furret hoothoot noctowl ledyba ledian spinarak ariados crobat chinchou lanturn pichu pichuspikyeared cleffa igglybuff togepi togetic natu xatu mareep flaaffy ampharos ampharosmega bellossom marill azumarill sudowoodo politoed hoppip skiploom jumpluff aipom sunkern sunflora yanma wooper quagsire espeon umbreon murkrow slowking slowkinggalar misdreavus unown wobbuffet girafarig pineco forretress dunsparce gligar steelix steelixmega snubbull granbull qwilfish qwilfishhisui scizor scizormega shuckle heracross heracrossmega sneasel sneaselhisui teddiursa ursaring slugma magcargo swinub piloswine corsola corsolagalar remoraid octillery delibird mantine skarmory houndour houndoom houndoommega kingdra phanpy donphan porygon2 stantler smeargle tyrogue hitmontop smoochum elekid magby miltank blissey raikou entei suicune larvitar pupitar tyranitar tyranitarmega lugia hooh celebi treecko grovyle sceptile sceptilemega torchic combusken blaziken blazikenmega mudkip marshtomp swampert swampertmega poochyena mightyena zigzagoon zigzagoongalar linoone linoonegalar wurmple silcoon beautifly cascoon dustox lotad lombre ludicolo seedot nuzleaf shiftry taillow swellow wingull pelipper ralts kirlia gardevoir gardevoirmega surskit masquerain shroomish breloom slakoth vigoroth slaking nincada ninjask shedinja whismur loudred exploud makuhita hariyama azurill nosepass skitty delcatty sableye sableyemega mawile mawilemega aron lairon aggron aggronmega meditite medicham medichammega electrike manectric manectricmega plusle minun volbeat illumise roselia gulpin swalot carvanha sharpedo sharpedomega wailmer wailord numel camerupt cameruptmega torkoal spoink grumpig spinda trapinch vibrava flygon cacnea cacturne swablu altaria altariamega zangoose seviper lunatone solrock barboach whiscash corphish crawdaunt baltoy claydol lileep cradily anorith armaldo feebas milotic castform castformsunny castformrainy castformsnowy kecleon shuppet banette banettemega duskull dusclops tropius chimecho absol absolmega wynaut snorunt glalie glaliemega spheal sealeo walrein clamperl huntail gorebyss relicanth luvdisc bagon shelgon salamence salamencemega beldum metang metagross metagrossmega regirock regice registeel latias latiasmega latios latiosmega kyogre kyogreprimal groudon groudonprimal rayquaza rayquazamega jirachi deoxys deoxysattack deoxysdefense deoxysspeed turtwig grotle torterra chimchar monferno infernape piplup prinplup empoleon starly staravia staraptor bidoof bibarel kricketot kricketune shinx luxio luxray budew roserade cranidos rampardos shieldon bastiodon burmy wormadam wormadamsandy wormadamtrash mothim combee vespiquen pachirisu buizel floatzel cherubi cherrim cherrimsunshine shellos gastrodon ambipom drifloon drifblim buneary lopunny lopunnymega mismagius honchkrow glameow purugly chingling stunky skuntank bronzor bronzong bonsly mimejr happiny chatot spiritomb gible gabite garchomp garchompmega munchlax riolu lucario lucariomega hippopotas hippowdon skorupi drapion croagunk toxicroak carnivine finneon lumineon mantyke snover abomasnow abomasnowmega weavile magnezone lickilicky rhyperior tangrowth electivire magmortar togekiss yanmega leafeon glaceon gliscor mamoswine porygonz gallade gallademega probopass dusknoir froslass rotom rotomheat rotomwash rotomfrost rotomfan rotommow uxie mesprit azelf dialga dialgaorigin palkia palkiaorigin heatran regigigas giratina giratinaorigin cresselia phione manaphy darkrai shaymin shayminsky arceus arceusbug arceusdark arceusdragon arceuselectric arceusfairy arceusfighting arceusfire arceusflying arceusghost arceusgrass arceusground arceusice arceuspoison arceuspsychic arceusrock arceussteel arceuswater arceuslegend victini snivy servine serperior tepig pignite emboar oshawott dewott samurott samurotthisui patrat watchog lillipup herdier stoutland purrloin liepard pansage simisage pansear simisear panpour simipour munna musharna pidove tranquill unfezant blitzle zebstrika roggenrola boldore gigalith woobat swoobat drilbur excadrill audino audinomega timburr gurdurr conkeldurr tympole palpitoad seismitoad throh sawk sewaddle swadloon leavanny venipede whirlipede scolipede cottonee whimsicott petilil lilligant lilliganthisui basculin basculinbluestriped basculinwhitestriped sandile krokorok krookodile darumaka darumakagalar darmanitan darmanitangalar darmanitanzen darmanitangalarzen maractus dwebble crustle scraggy scrafty sigilyph yamask yamaskgalar cofagrigus tirtouga carracosta archen archeops trubbish garbodor garbodorgmax zorua zoruahisui zoroark zoroarkhisui minccino cinccino gothita gothorita gothitelle solosis duosion reuniclus ducklett swanna vanillite vanillish vanilluxe deerling sawsbuck emolga karrablast escavalier foongus amoonguss frillish frillishfemale jellicent jellicentfemale alomomola joltik galvantula ferroseed ferrothorn klink klang klinklang tynamo eelektrik eelektross elgyem beheeyem litwick lampent chandelure axew fraxure haxorus cubchoo beartic cryogonal shelmet accelgor stunfisk stunfiskgalar mienfoo mienshao druddigon golett golurk pawniard bisharp bouffalant rufflet braviary braviaryhisui vullaby mandibuzz heatmor durant deino zweilous hydreigon larvesta volcarona cobalion terrakion virizion tornadus tornadustherian thundurus thundurustherian reshiram zekrom landorus landorustherian kyurem kyuremblack kyuremwhite keldeo keldeoresolute meloetta meloettapirouette genesect genesectdouse genesectshock genesectburn genesectchill chespin quilladin chesnaught fennekin braixen delphox froakie frogadier greninja greninjaash bunnelby diggersby fletchling fletchinder talonflame scatterbug spewpa vivillon vivillonfancy vivillonpokeball litleo pyroar flabebe floette floetteeternal florges skiddo gogoat pancham pangoro furfrou espurr meowstic meowsticf honedge doublade aegislash aegislashblade spritzee aromatisse swirlix slurpuff inkay malamar binacle barbaracle skrelp dragalge clauncher clawitzer helioptile heliolisk tyrunt tyrantrum amaura aurorus sylveon hawlucha dedenne carbink goomy sliggoo sliggoohisui goodra goodrahisui klefki phantump trevenant pumpkaboo pumpkaboosmall pumpkaboolarge pumpkaboosuper gourgeist gourgeistsmall gourgeistlarge gourgeistsuper bergmite avalugg avalugghisui noibat noivern xerneas xerneasneutral yveltal zygarde zygarde10 zygardecomplete diancie dianciemega hoopa hoopaunbound volcanion rowlet dartrix decidueye decidueyehisui litten torracat incineroar popplio brionne primarina pikipek trumbeak toucannon yungoos gumshoos gumshoostotem grubbin charjabug vikavolt vikavolttotem crabrawler crabominable oricorio oricoriopompom oricoriopau oricoriosensu cutiefly ribombee ribombeetotem rockruff lycanroc lycanrocmidnight lycanrocdusk wishiwashi wishiwashischool mareanie toxapex mudbray mudsdale dewpider araquanid araquanidtotem fomantis lurantis lurantistotem morelull shiinotic salandit salazzle salazzletotem stufful bewear bounsweet steenee tsareena comfey oranguru passimian wimpod golisopod sandygast palossand pyukumuku typenull silvally silvallybug silvallydark silvallydragon silvallyelectric silvallyfairy silvallyfighting silvallyfire silvallyflying silvallyghost silvallygrass silvallyground silvallyice silvallypoison silvallypsychic silvallyrock silvallysteel silvallywater minior miniormeteor komala turtonator togedemaru togedemarutotem mimikyu mimikyubusted mimikyutotem mimikyubustedtotem bruxish drampa dhelmise jangmoo hakamoo kommoo kommoototem tapukoko tapulele tapubulu tapufini cosmog cosmoem solgaleo lunala nihilego buzzwole pheromosa xurkitree celesteela kartana guzzlord necrozma necrozmaduskmane necrozmadawnwings necrozmaultra magearna magearnaoriginal marshadow poipole naganadel stakataka blacephalon zeraora meltan melmetal melmetalgmax grookey thwackey rillaboom rillaboomgmax scorbunny raboot cinderace cinderacegmax sobble drizzile inteleon inteleongmax skwovet greedent rookidee corvisquire corviknight corviknightgmax blipbug dottler orbeetle orbeetlegmax nickit thievul gossifleur eldegoss wooloo dubwool chewtle drednaw drednawgmax yamper boltund rolycoly carkol coalossal coalossalgmax applin flapple flapplegmax appletun appletungmax silicobra sandaconda sandacondagmax cramorant cramorantgulping cramorantgorging arrokuda barraskewda toxel toxtricity toxtricitylowkey toxtricitygmax toxtricitylowkeygmax sizzlipede centiskorch centiskorchgmax clobbopus grapploct sinistea sinisteaantique polteageist polteageistantique hatenna hattrem hatterene hatterenegmax impidimp morgrem grimmsnarl grimmsnarlgmax obstagoon perrserker cursola sirfetchd mrrime runerigus milcery alcremie alcremiegmax falinks pincurchin snom frosmoth stonjourner eiscue eiscuenoice indeedee indeedeef morpeko morpekohangry cufant copperajah copperajahgmax dracozolt arctozolt dracovish arctovish duraludon duraludongmax dreepy drakloak dragapult zacian zaciancrowned zamazenta zamazentacrowned eternatus eternatuseternamax kubfu urshifu urshifurapidstrike urshifugmax urshifurapidstrikegmax zarude zarudedada regieleki regidrago glastrier spectrier calyrex calyrexice calyrexshadow wyrdeer kleavor ursaluna basculegion basculegionf sneasler overqwil enamorus enamorustherian pokestarsmeargle pokestarufo pokestarufo2 pokestarbrycenman pokestarmt pokestarmt2 pokestartransport pokestargiant pokestarhumanoid pokestarmonster pokestarf00 pokestarf002 pokestarspirit pokestarblackdoor pokestarwhitedoor pokestarblackbelt pokestarufopropu2')


ItemsEnum = Enum('ItemsEnum', 'abomasite absolite absorbbulb adamantorb adrenalineorb aerodactylite aggronite aguavberry airballoon alakazite aloraichiumz altarianite ampharosite apicotberry armorfossil aspearberry assaultvest audinite babiriberry banettite beastball beedrillite belueberry berry berryjuice berrysweet berserkgene bigroot bindingband bitterberry blackbelt blackglasses blacksludge blastoisinite blazikenite blueorb blukberry blunderpolicy bottlecap brightpowder buggem bugmemory buginiumz burndrive burntberry cameruptite cellbattery charcoal charizarditex charizarditey chartiberry cheriberry cherishball chestoberry chilanberry chilldrive chippedpot choiceband choicescarf choicespecs chopleberry clawfossil cloversweet cobaberry colburberry cornnberry coverfossil crucibellite crackedpot custapberry damprock darkgem darkmemory darkiniumz dawnstone decidiumz deepseascale deepseatooth destinyknot diancite diveball domefossil dousedrive dracoplate dragonfang dragongem dragonmemory dragonscale dragoniumz dreadplate dreamball dubiousdisc durinberry duskball duskstone earthplate eeviumz ejectbutton ejectpack electirizer electricgem electricmemory electricseed electriumz energypowder enigmaberry eviolite expertbelt fairiumz fairygem fairymemory fastball fightinggem fightingmemory fightiniumz figyberry firegem firememory firestone firiumz fistplate flameorb flameplate floatstone flowersweet flyinggem flyingmemory flyiniumz focusband focussash fossilizedbird fossilizeddino fossilizeddrake fossilizedfish friendball fullincense fullrestore galaricacuff galaricawreath galladite ganlonberry garchompite gardevoirite gengarite ghostgem ghostmemory ghostiumz glalitite goldberry goldbottlecap grassgem grassmemory grassiumz grassyseed greatball grepaberry gripclaw griseousorb groundgem groundmemory groundiumz gyaradosite habanberry hardstone healball heatrock heavyball heavydutyboots helixfossil heracronite hondewberry houndoominite hyperpotion iapapaberry iceberry icegem icememory icestone icicleplate iciumz icyrock inciniumz insectplate ironball ironplate jabocaberry jawfossil kangaskhanite kasibberry kebiaberry keeberry kelpsyberry kingsrock kommoniumz laggingtail lansatberry latiasite latiosite laxincense leafstone leek leftovers leppaberry levelball liechiberry lifeorb lightball lightclay lopunnite loveball lovesweet lucarionite luckypunch lumberry luminousmoss lunaliumz lureball lustrousorb luxuryball lycaniumz machobrace magmarizer magnet magoberry magostberry mail manectite marangaberry marshadiumz masterball mawilite maxpotion meadowplate medichamite mentalherb metagrossite metalcoat metalpowder metronome mewniumz mewtwonitex mewtwonitey micleberry mimikiumz mindplate mintberry miracleberry miracleseed mistyseed moonball moonstone muscleband mysteryberry mysticwater nanabberry nestball netball nevermeltice nomelberry normalgem normaliumz occaberry oddincense oldamber oranberry ovalstone przcureberry psncureberry pamtreberry parkball passhoberry payapaberry pechaberry persimberry petayaberry pidgeotite pikaniumz pikashuniumz pinapberry pinkbow pinsirite pixieplate plumefossil poisonbarb poisongem poisonmemory poisoniumz pokeball polkadotbow pomegberry poweranklet powerband potion powerbelt powerbracer powerherb powerlens powerweight premierball primariumz prismscale protectivepads protector psychicgem psychicmemory psychicseed psychiumz qualotberry quickball quickclaw quickpowder rabutaberry rarebone rawstberry razorclaw razorfang razzberry reapercloth redcard redorb repeatball ribbonsweet rindoberry ringtarget rockgem rockincense rockmemory rockiumz roseincense rockyhelmet roomservice rootfossil roseliberry rowapberry rustedshield rustedsword sablenite sachet safariball safetygoggles sailfossil salacberry salamencite sceptilite scizorite scopelens seaincense sharpbeak sharpedonite shedshell shellbell shinystone shockdrive shucaberry silkscarf silverpowder sitrusberry skullfossil skyplate slowbronite smoothrock snorliumz snowball softsand solganiumz souldew spelltag spelonberry splashplate spookyplate sportball starfberry steelgem steelmemory steeliumz starsweet steelixite stick stickybarb stoneplate strawberrysweet sunstone superpotion swampertite sweetapple tamatoberry tangaberry tapuniumz tartapple terrainextender thickclub throatspray thunderstone timerball toxicorb toxicplate twistedspoon tyranitarite ultraball ultranecroziumz upgrade utilityumbrella venusaurite vilevial wacanberry watergem watermemory waterstone wateriumz watmelberry waveincense weaknesspolicy wepearberry whippeddream whiteherb widelens wikiberry wiseglasses yacheberry zapplate zoomlens acrobike adventureguide apricornbox aquasuit auroraticket autograph azureflute bandautograph basementkey berrypots berrypouch bicycle bikevoucher bluecard bluepetal campinggear cardkey catchingcharm clearbell coincase colressmchn contestcostume contestpass coupon1 coupon2 coupon3 dnasplicers darkstone devongoods devonparts devonscope devonscubagear dowsingmchn dowsingmachine dragonskull droppeditem dynamaxband eggcard elevatorkey endorsement enigmastone enigmaticcard eonflute eonticket escaperope expshare explorerkit famechecker fashioncase fishingrod foragebag gbsounds gsball galactickey gogoggles godstone goldteeth goodrod gracidea gram1 gram2 gram3 greenpetal grubbyhanky hitechearbuds holocaster honorofkalos ilimasnormaliumz intriguingstone itemfinder jadeorb journal keystone keytoroom1 keytoroom2 keytoroom4 keytoroom6 leftpokeball legendplate lenscase letter libertypass liftkey lightstone lockcapsule lookerticket lootsack lostitem lunarwing machbike machinepart magmaemblem magmastone magmasuit makeupbag medalbox megabracelet megaring membercard meteorite meteoriteshard moonflute mysteryegg mysticticket nlunarizer nsolarizer oaksletter oaksparcel oldcharm oldletter oldrod oldseamap orangepetal ovalcharm pairoftickets palpad parcel pass permit photoalbum pinkpetal plasmacard poffincase pointcard pokeradar pokeblockkit pokeblockcase pokeflute pokemonboxlink powderjar powerplantpass prisonbottle profsletter professorsmask propcase purplepetal ragecandybar rainbowflower rainbowpass rainbowwing redchain redpetal redscale revealglass ridepager rm1key rm2key rm4key rm6key rollerskates rotombike rotomcatalog ruby rulebook ssticket sapphire scanner sealbag sealcase secretkey secretpotion shinycharm silphscope silverwing slowpoketail soniasbook sootsack sparklingstone sprayduck sprinklotad squirtbottle storagekey suitekey sunflute superrod surgebadge tmcase tmvpass tea teachytv tidalbell townmap traveltrunk tripass unownreport vsrecorder vsseeker wailmerpail wishingstar workskey xtransceiver yellowpetal zpowering zring zygardecube')


MovesEnum = Enum('MovesEnum', 'tenmillionvoltthunderbolt absorb accelerock acid acidarmor aciddownpour acidspray acrobatics acupressure aerialace aeroblast afteryou agility aircutter airslash alloutpummeling allyswitch amnesia anchorshot ancientpower appleacid aquajet aquaring aquatail armthrust aromatherapy aromaticmist assist assurance astralbarrage astonish attackorder attract aurasphere aurawheel aurorabeam auroraveil autotomize avalanche babydolleyes baddybad banefulbunker barbbarrage barrage barrier batonpass beakblast beatup belch behemothbash behemothblade bellydrum bestow bide bind bite bittermalice blackholeeclipse blastburn blazekick bleakwindstorm blizzard block bloomdoom blueflare bodypress bodyslam boltbeak boltstrike boneclub bonerush bonemerang boomburst bounce bouncybubble bravebird branchpoke breakingswipe breakneckblitz brickbreak brine brutalswing bubble bubblebeam bugbite bugbuzz bulkup bulldoze bulletpunch bulletseed burningjealousy burnup buzzybuzz calmmind camouflage captivate catastropika ceaselessedge celebrate charge chargebeam charm chatter chipaway chloroblast circlethrow clamp clangingscales clangoroussoul clangoroussoulblaze clearsmog closecombat coaching coil cometpunch confide confuseray confusion constrict continentalcrush conversion conversion2 copycat coreenforcer corkscrewcrash corrosivegas cosmicpower cottonguard cottonspore counter courtchange covet crabhammer craftyshield crosschop crosspoison crunch crushclaw crushgrip curse cut darkpulse darkvoid darkestlariat dazzlinggleam decorate defendorder defensecurl defog destinybond detect devastatingdrake diamondstorm dig direclaw disable disarmingvoice discharge dive dizzypunch doomdesire doublehit doubleironbash doublekick doubleslap doubleteam doubleedge dracometeor dragonascent dragonbreath dragonclaw dragondance dragondarts dragonenergy dragonhammer dragonpulse dragonrage dragonrush dragontail drainpunch drainingkiss dreameater drillpeck drillrun drumbeating dualchop dynamicpunch dualwingbeat dynamaxcannon earthpower earthquake echoedvoice eerieimpulse eeriespell eggbomb electricterrain electrify electroball electroweb embargo ember encore endeavor endure energyball entrainment eruption esperwing eternabeam expandingforce explosion extrasensory extremeevoboost extremespeed facade fairylock fairywind fakeout faketears falsesurrender falseswipe featherdance feint feintattack fellstinger fierydance fierywrath finalgambit fireblast firefang firelash firepledge firepunch firespin firstimpression fishiousrend fissure flail flameburst flamecharge flamewheel flamethrower flareblitz flash flashcannon flatter fleurcannon fling flipturn floatyfall floralhealing flowershield fly flyingpress focusblast focusenergy focuspunch followme forcepalm foresight forestscurse foulplay freezeshock freezedry freezingglare freezyfrost frenzyplant frostbreath frustration furyattack furycutter furyswipes fusionbolt fusionflare futuresight gastroacid geargrind gearup genesissupernova geomancy gigadrain gigaimpact gigavolthavoc glaciallance glaciate glare glitzyglow gmaxbefuddle gmaxcannonade gmaxcentiferno gmaxchistrike gmaxcuddle gmaxdepletion gmaxdrumsolo gmaxfinale gmaxtartness gmaxvinelash gmaxvolcalith gmaxvoltcrash gmaxwildfire gmaxwindrage gmaxfireball gmaxfoamburst gmaxgoldrush gmaxgravitas gmaxhydrosnipe gmaxmalodor gmaxmeltdown gmaxstonesurge gmaxstunshock gmaxsweetness gmaxterror gmaxoneblow gmaxrapidflow gmaxreplenish gmaxresonance gmaxsandblast gmaxsmite gmaxsnooze gmaxsteelsurge grassknot grasspledge grasswhistle grassyglide grassyterrain gravapple gravity growl growth grudge guardsplit guardswap guardianofalola guillotine gunkshot gust gyroball hail hammerarm happyhour harden haze headcharge headsmash headbutt headlongrush healbell healblock healorder healpulse healingwish heartstamp heartswap heatcrash heatwave heavyslam helpinghand hex hiddenpower hiddenpowerbug hiddenpowerdark hiddenpowerdragon hiddenpowerelectric hiddenpowerfighting hiddenpowerfire hiddenpowerflying hiddenpowerghost hiddenpowergrass hiddenpowerground hiddenpowerice hiddenpowerpoison hiddenpowerpsychic hiddenpowerrock hiddenpowersteel hiddenpowerwater highhorsepower highjumpkick holdback holdhands honeclaws hornattack horndrill hornleech howl hurricane hydrocannon hydropump hydrovortex hyperbeam hyperfang hypervoice hyperspacefury hyperspacehole hypnosis iceball icebeam iceburn icefang icehammer icepunch iceshard iciclecrash iciclespear icywind imprison incinerate infernalparade inferno infernooverdrive infestation ingrain instruct iondeluge irondefense ironhead irontail jawlock judgment jumpkick junglehealing karatechop kinesis kingsshield knockoff landswrath laserfocus lashout lastresort lavaplume leafblade leafstorm leaftornado leafage leechlife leechseed leer letssnuggleforever lick lightscreen lightthatburnsthesky lifedew lightofruin liquidation lockon lovelykiss lowkick lowsweep luckychant lunarblessing lunardance lunge lusterpurge machpunch magiccoat magicpowder magicroom magicalleaf magikarpsrevenge magmastorm magnetbomb magnetrise magneticflux magnitude maliciousmoonsault matblock mefirst maxairstream maxdarkness maxflare maxflutterby maxgeyser maxguard meanlook maxhailstorm maxknuckle maxlightning maxmindstorm maxooze maxovergrowth maxphantasm maxquake maxrockfall maxstarfall maxsteelspike maxstrike maxwyrmwind meditate megadrain megakick megapunch megahorn memento menacingmoonrazemaelstrom metalburst metalclaw metalsound meteorassault meteorbeam meteormash metronome milkdrink mimic mindblown mindreader minimize miracleeye mirrorcoat mirrormove mirrorshot mist mistball mistyexplosion mistyterrain moonblast moongeistbeam moonlight morningsun mountaingale mudbomb mudshot mudsport mudslap muddywater multiattack mysticalfire mysticalpower nastyplot naturalgift naturepower naturesmadness needlearm neverendingnightmare nightdaze nightshade nightslash nightmare nobleroar noretreat nuzzle oblivionwing obstruct oceanicoperetta octazooka octolock odorsleuth ominouswind originpulse outrage overdrive overheat painsplit paleowave paraboliccharge partingshot payday payback peck perishsong petalblizzard petaldance phantomforce photongeyser pikapapow pinmissile plasmafists playnice playrough pluck poisonfang poisongas poisonjab poisonpowder poisonsting poisontail pollenpuff poltergeist pound powder powdersnow powergem powershift powersplit powerswap powertrick powertrip powerwhip poweruppunch precipiceblades present prismaticlaser protect psybeam psychup psychic psychicfangs psychicterrain psychoboost psychocut psychoshift psyshieldbash psyshock psystrike psywave pulverizingpancake punishment purify pursuit pyroball quash quickattack quickguard quiverdance rage ragepowder ragingfury raindance rapidspin razorleaf razorshell razorwind recover recycle reflect reflecttype refresh relicsong rest retaliate return revelationdance revenge reversal risingvoltage roar roaroftime rockblast rockclimb rockpolish rockslide rocksmash rockthrow rocktomb rockwrecker roleplay rollingkick rollout roost rototiller round sacredfire sacredsword safeguard sandattack sandtomb sandsearstorm sandstorm sappyseed savagespinout scald scaleshot scaryface scorchingsands scratch screech searingshot searingsunrazesmash secretpower secretsword seedbomb seedflare seismictoss selfdestruct shadowball shadowbone shadowclaw shadowforce shadowpunch shadowsneak shadowstrike sharpen shatteredpsyche sheercold shellsidearm shellsmash shelltrap shelter shiftgear shockwave shoreup signalbeam silverwind simplebeam sing sinisterarrowraid sizzlyslide sketch skillswap skittersmack skullbash skyattack skydrop skyuppercut slackoff slam slash sleeppowder sleeptalk sludge sludgebomb sludgewave smackdown smartstrike smellingsalts smog smokescreen snaptrap snarl snatch snipeshot snore soak softboiled solarbeam solarblade sonicboom soulstealing7starstrike spacialrend spark sparklingaria sparklyswirl spectralthief speedswap spiderweb spikecannon spikes spikyshield spiritbreak spiritshackle spitup spite splash splinteredstormshards splishysplash spore spotlight springtidestorm stealthrock steameruption steamroller steelbeam steelroller steelwing stickyweb stockpile stokedsparksurfer stomp stompingtantrum stoneaxe stoneedge storedpower stormthrow strangesteam strength strengthsap stringshot struggle strugglebug stuffcheeks stunspore submission substitute subzeroslammer suckerpunch sunnyday sunsteelstrike superfang superpower supersonic supersonicskystrike surf surgingstrikes swagger swallow sweetkiss sweetscent swift switcheroo swordsdance synchronoise synthesis tackle tailglow tailslap tailwhip tailwind takedown takeheart tarshot taunt tearfullook teatime technoblast tectonicrage teeterdance telekinesis teleport terrainpulse thief thousandarrows thousandwaves thrash throatchop thunder thundercage thunderfang thunderouskick thunderpunch thundershock thunderwave thunderbolt tickle topsyturvy torment toxic toxicspikes toxicthread transform triattack trick trickroom trickortreat triplearrows tripleaxel triplekick tropkick trumpcard twineedle twinkletackle twister uturn uproar vcreate vacuumwave veeveevolley venomdrench venoshock victorydance vinewhip visegrip vitalthrow voltswitch volttackle wakeupslap watergun waterpledge waterpulse watershuriken watersport waterspout waterfall wavecrash weatherball whirlpool whirlwind wickedblow wideguard wildboltstorm wildcharge willowisp wingattack wish withdraw wonderroom woodhammer workup worryseed wrap wringout xscissor yawn zapcannon zenheadbutt zingzap zippyzap')


TypesEnum = Enum('TypesEnum', 'bug dark dragon electric fairy fighting fire flying ghost grass ground ice normal poison psychic rock steel water')


Query = TypedDict('Query', {
	'getAbility': 'GetAbilityQueryResult',
	'getFuzzyAbility': 'GetFuzzyAbilityQueryResult',
	'getPokemonByDexNumber': 'GetPokemonByDexNumberQueryResult',
	'getPokemon': 'GetPokemonQueryResult',
	'getFuzzyPokemon': 'GetFuzzyPokemonQueryResult',
	'getAllPokemonSpecies': 'GetAllPokemonSpeciesQueryResult',
	'getItem': 'GetItemQueryResult',
	'getFuzzyItem': 'GetFuzzyItemQueryResult',
	'getLearnset': 'GetLearnsetQueryResult',
	'getFuzzyLearnset': 'GetFuzzyLearnsetQueryResult',
	'getMove': 'GetMoveQueryResult',
	'getFuzzyMove': 'GetFuzzyMoveQueryResult',
	'getTypeMatchup': 'GetTypeMatchupQueryResult',
})


GetAbilityParams = TypedDict('GetAbilityParams', {
	'ability': 'AbilitiesEnum',
})


GetAbilityQueryResult = ClassVar['Ability']


GetFuzzyAbilityParams = TypedDict('GetFuzzyAbilityParams', {
	'offset': Optional[int],
	'take': Optional[int],
	'reverse': Optional[bool],
	'ability': str,
})


GetFuzzyAbilityQueryResult = ClassVar[List['Ability']]


GetPokemonByDexNumberParams = TypedDict('GetPokemonByDexNumberParams', {
	'offsetFlavorTexts': Optional[int],
	'takeFlavorTexts': Optional[int],
	'reverseFlavorTexts': Optional[bool],
	'number': int,
})


GetPokemonByDexNumberQueryResult = ClassVar['Pokemon']


GetPokemonParams = TypedDict('GetPokemonParams', {
	'offsetFlavorTexts': Optional[int],
	'takeFlavorTexts': Optional[int],
	'reverseFlavorTexts': Optional[bool],
	'pokemon': 'PokemonEnum',
})


GetPokemonQueryResult = ClassVar['Pokemon']


GetFuzzyPokemonParams = TypedDict('GetFuzzyPokemonParams', {
	'offset': Optional[int],
	'take': Optional[int],
	'reverse': Optional[bool],
	'pokemon': str,
	'offsetFlavorTexts': Optional[int],
	'takeFlavorTexts': Optional[int],
	'reverseFlavorTexts': Optional[bool],
})


GetFuzzyPokemonQueryResult = ClassVar[List['Pokemon']]


GetAllPokemonSpeciesParams = TypedDict('GetAllPokemonSpeciesParams', {
	'offset': Optional[int],
	'take': Optional[int],
	'reverse': Optional[bool],
})


GetAllPokemonSpeciesQueryResult = ClassVar[List[str]]


GetItemParams = TypedDict('GetItemParams', {
	'item': 'ItemsEnum',
})


GetItemQueryResult = ClassVar['Item']


GetFuzzyItemParams = TypedDict('GetFuzzyItemParams', {
	'offset': Optional[int],
	'take': Optional[int],
	'reverse': Optional[bool],
	'item': str,
})


GetFuzzyItemQueryResult = ClassVar[List['Item']]


GetLearnsetParams = TypedDict('GetLearnsetParams', {
	'generation': Optional[int],
	'moves': List['MovesEnum'],
	'pokemon': 'PokemonEnum',
})


GetLearnsetQueryResult = ClassVar['Learnset']


GetFuzzyLearnsetParams = TypedDict('GetFuzzyLearnsetParams', {
	'generation': Optional[int],
	'moves': List[str],
	'pokemon': str,
})


GetFuzzyLearnsetQueryResult = ClassVar['Learnset']


GetMoveParams = TypedDict('GetMoveParams', {
	'move': 'MovesEnum',
})


GetMoveQueryResult = ClassVar['Move']


GetFuzzyMoveParams = TypedDict('GetFuzzyMoveParams', {
	'offset': Optional[int],
	'take': Optional[int],
	'reverse': Optional[bool],
	'move': str,
})


GetFuzzyMoveQueryResult = ClassVar[List['Move']]


GetTypeMatchupParams = TypedDict('GetTypeMatchupParams', {
	'types': List['TypesEnum'],
})


GetTypeMatchupQueryResult = ClassVar['TypeMatchup']


Ability = TypedDict('Ability', {
	'key': 'AbilitiesEnum',
	'bulbapediaPage': str,
	'desc': Optional[str],
	'isFieldAbility': Optional[str],
	'name': str,
	'serebiiPage': str,
	'shortDesc': str,
	'smogonPage': str,
})


Pokemon = TypedDict('Pokemon', {
	'key': 'PokemonEnum',
	'abilities': 'Abilities',
	'backSprite': str,
	'baseForme': Optional[str],
	'baseSpecies': Optional[str],
	'baseStats': 'Stats',
	'baseStatsTotal': int,
	'bulbapediaPage': str,
	'catchRate': Optional['CatchRate'],
	'color': str,
	'cosmeticFormes': Optional[List[str]],
	'eggGroups': Optional[List[str]],
	'evolutionLevel': Optional[str],
	'evolutions': Optional[List['Pokemon']],
	'evYields': 'EvYields',
	'flavorTexts': List['Flavor'],
	'forme': Optional[str],
	'formeLetter': Optional[str],
	'gender': 'Gender',
	'height': float,
	'isEggObtainable': bool,
	'levellingRate': Optional[str],
	'maximumHatchTime': Optional[int],
	'minimumHatchTime': Optional[int],
	'num': int,
	'otherFormes': Optional[List[str]],
	'preevolutions': Optional[List['Pokemon']],
	'serebiiPage': str,
	'shinyBackSprite': str,
	'shinySprite': str,
	'smogonPage': str,
	'smogonTier': str,
	'species': str,
	'sprite': str,
	'types': List[str],
	'weight': float,
})


Abilities = TypedDict('Abilities', {
	'first': str,
	'hidden': Optional[str],
	'second': Optional[str],
	'special': Optional[str],
})


Stats = TypedDict('Stats', {
	'attack': int,
	'defense': int,
	'hp': int,
	'specialattack': int,
	'specialdefense': int,
	'speed': int,
})


CatchRate = TypedDict('CatchRate', {
	'base': int,
	'percentageWithOrdinaryPokeballAtFullHealth': str,
})


EvYields = TypedDict('EvYields', {
	'attack': int,
	'defense': int,
	'hp': int,
	'specialattack': int,
	'specialdefense': int,
	'speed': int,
})


Flavor = TypedDict('Flavor', {
	'flavor': str,
	'game': str,
})


Gender = TypedDict('Gender', {
	'female': str,
	'male': str,
})


Item = TypedDict('Item', {
	'key': 'ItemsEnum',
	'bulbapediaPage': str,
	'desc': str,
	'generationIntroduced': int,
	'isNonstandard': Optional[str],
	'name': str,
	'serebiiPage': str,
	'shortDesc': Optional[str],
	'smogonPage': Optional[str],
	'sprite': str,
})


Learnset = TypedDict('Learnset', {
	'backSprite': str,
	'color': str,
	'dreamworldMoves': Optional[List['LearnsetMove']],
	'eggMoves': Optional[List['LearnsetMove']],
	'eventMoves': Optional[List['LearnsetMove']],
	'levelUpMoves': Optional[List['LearnsetLevelUpMove']],
	'pokemonKey': 'PokemonEnum',
	'num': int,
	'shinyBackSprite': str,
	'shinySprite': str,
	'species': str,
	'sprite': str,
	'tmMoves': Optional[List['LearnsetMove']],
	'tutorMoves': Optional[List['LearnsetMove']],
	'virtualTransferMoves': Optional[List['LearnsetMove']],
})


LearnsetMove = TypedDict('LearnsetMove', {
	'generation': Optional[int],
	'name': Optional[str],
})


LearnsetLevelUpMove = TypedDict('LearnsetLevelUpMove', {
	'generation': Optional[int],
	'name': Optional[str],
	'level': Optional[int],
})


Move = TypedDict('Move', {
	'key': 'MovesEnum',
	'accuracy': int,
	'basePower': str,
	'bulbapediaPage': str,
	'category': str,
	'contestType': Optional[str],
	'desc': Optional[str],
	'isFieldMove': Optional[str],
	'isGMax': Optional[str],
	'isNonstandard': Optional[str],
	'isZ': Optional[str],
	'maxMovePower': Optional[int],
	'name': str,
	'pp': int,
	'priority': int,
	'serebiiPage': str,
	'shortDesc': str,
	'smogonPage': str,
	'target': str,
	'type': str,
	'zMovePower': int,
})


TypeMatchup = TypedDict('TypeMatchup', {
	'attacking': 'Type',
	'defending': 'Type',
})


Type = TypedDict('Type', {
	'doubleEffectiveTypes': List[str],
	'doubleResistedTypes': List[str],
	'effectiveTypes': List[str],
	'effectlessTypes': List[str],
	'normalTypes': List[str],
	'resistedTypes': List[str],
})



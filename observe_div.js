mydocs = document.querySelector("#mainContainer > div.app-main-container.flex.layout-row.explorer-v3 > div > div.sc-llYToB.bepCke > main > div.sc-ewSSRw.fDTLhF > div.sc-eicnZh.bSQUzR > div.sc-fvxABq.eCsope.explorer-file-list-virtualized__container.explorer-file-list-virtualized__container-a > div:nth-child(1) > div")

DocumentObserverConfig = {
    attributes: true, 
    childList: true, 
    characterData: true,
    subtree: true
};

hrefs = []
DocumentObserver = new MutationObserver(function() {
    var items = mydocs.getElementsByTagName('a')
    for (let i of items ){
        hrefs.push(i.href)
    }
});

DocumentObserver.observe(mydocs, DocumentObserverConfig)

function unique (arr) {
    return Array.from(new Set(arr))
}

result = unique(hrefs)
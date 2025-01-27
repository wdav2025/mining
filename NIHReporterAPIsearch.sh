#Search the NIHReporter Database for All Training Grants
curl -s "
{
  "criteria":{ advanced_text_search: { operator: "and",
search_field: "projecttitle,abstracttext,terms", "search_text": "brain
disorder" 
  {
"funding_mechanism":["F","K","T","R", "U"],
"newly_added_projects_only": false,
},
"include_fields": [
"FiscalYear","ProjectNum","Organization", "OrganizationType",
"AwardType", "ActivityCode", "AwardAmount", "PrincipalInvestigators", 
"AgencyIcAdmin", "AgencyIcFundings", "AwardNoticeDate", "CoreProjectNum", "ProjectTitle",
"BudgetStart",,"DirectCostAmt","IndirectCostAmt"
],
"offset":0,
"limit":25,
"sort_field":"project_start_date",
"sort_order":"desc"
}

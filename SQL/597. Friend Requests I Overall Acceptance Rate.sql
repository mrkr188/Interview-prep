-- In social network like Facebook or Twitter, people send friend requests and accept others’ requests as well. Now given two tables as below:
 

-- Table: friend_request
-- | sender_id | send_to_id |request_date|
-- |-----------|------------|------------|
-- | 1         | 2          | 2016_06-01 |
-- | 1         | 3          | 2016_06-01 |
-- | 1         | 4          | 2016_06-01 |
-- | 2         | 3          | 2016_06-02 |
-- | 3         | 4          | 2016-06-09 |
 

-- Table: request_accepted
-- | requester_id | accepter_id |accept_date |
-- |--------------|-------------|------------|
-- | 1            | 2           | 2016_06-03 |
-- | 1            | 3           | 2016-06-08 |
-- | 2            | 3           | 2016-06-08 |
-- | 3            | 4           | 2016-06-09 |
-- | 3            | 4           | 2016-06-10 |
 

-- Write a query to find the overall acceptance rate of requests rounded to 2 decimals, which is the number of acceptance divide the number of requests.
 

-- For the sample data above, your query should return the following result.
 

-- |accept_rate|
-- |-----------|
-- |       0.80|
 

-- Note:
-- The accepted requests are not necessarily from the table friend_request. In this case, you just need to simply count the total accepted requests (no matter whether they are in the original requests), and divide it by the number of requests to get the acceptance rate.
-- It is possible that a sender sends multiple requests to the same receiver, and a request could be accepted more than once. In this case, the ‘duplicated’ requests or acceptances are only counted once.
-- If there is no requests at all, you should return 0.00 as the accept_rate.
 

-- Explanation: There are 4 unique accepted requests, and there are 5 requests in total. So the rate is 0.80.
 

-- Follow-up:
-- Can you write a query to return the accept rate but for every month?
-- How about the cumulative accept rate for every day?


select round(ifnull(
                    (select count(*) from (select distinct requester_id, accepter_id from request_accepted) as a)/
                    (select count(*) from (select distinct sender_id, send_to_id from friend_request) as b), 
                    0.00), 
              2) as accept_rate


select ifnull(round((count(distinct requester_id,accepter_id)/count(distinct sender_id,send_to_id)),2), 0.00) as accept_rate
from friend_request, request_accepted


-- follow up - accept rate but for every month
select if(d.req =0, 0.00, round(c.acp/d.req,2)) as accept_rate, c.month from 
(select count(distinct requester_id, accepter_id) as acp, Month(accept_date) as month from request_accepted) c, 
(select count(distinct sender_id, send_to_id) as req, Month(request_date) as month from friend_request) d 
where c.month = d.month 
group by c.month


-- https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/discuss/358575/Detailed-Explaination-for-Question-and-2-follow-up
-- follow up - umulative accept rate for every day
select s.date1, ifnull(round(sum(case when t.ind = 'a' then t.cnt else 0 end)/sum(case when t.ind = 'r' then t.cnt else 0 end),2),0) 
from
      (select distinct x.request_date as date1 from friend_request x
       union 
      select distinct y.accept_date as date1 from request_accepted y 
      ) s
left join 
      (select v.request_date as date1, count(*) as cnt,'r' as ind from friend_request v group by v.request_date
       union all
      select w.accept_date as date1, count(*) as cnt,'a' as ind from request_accepted w group by w.accept_date) t
## s.date1 >= t.date1, which for each reacord in s, it will join with all records earlier than it in t
on s.date1 >= t.date1
# group by s.date1 then we can get a cumulative result to that day
group by s.date1
order by s.date1

# EMA Hourly Continuation — XRP/USDT P26_100

**Symbol:** XRP/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.7208 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0170 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -2.1158 |
| sortino_ratio | -0.6288 |
| max_drawdown | 0.5627 |
| cagr | -0.2497 |
| net_avg_win | 61.4174 |
| net_avg_loss | -86.4107 |
| avg_hold_time_bars | 15.6200 |
| exposure | 0.3046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

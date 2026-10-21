# EMA Hourly Continuation — ARKM/USDT P26_34

**Symbol:** ARKM/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 209 |
| net_profit_factor | 0.6239 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.8358 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -2.2578 |
| sortino_ratio | -0.4650 |
| max_drawdown | 0.4430 |
| cagr | -0.1927 |
| net_avg_win | 73.4017 |
| net_avg_loss | -96.1598 |
| avg_hold_time_bars | 5.2249 |
| exposure | 0.0496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

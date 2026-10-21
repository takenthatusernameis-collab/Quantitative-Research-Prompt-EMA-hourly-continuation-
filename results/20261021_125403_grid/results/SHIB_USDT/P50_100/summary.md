# EMA Hourly Continuation — SHIB/USDT P50_100

**Symbol:** SHIB/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6593 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.9146 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -2.5868 |
| sortino_ratio | -0.6773 |
| max_drawdown | 0.5601 |
| cagr | -0.2670 |
| net_avg_win | 66.3342 |
| net_avg_loss | -89.3063 |
| avg_hold_time_bars | 9.2262 |
| exposure | 0.1409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — SHIB/USDT P12_21

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.6418 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9469 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -2.2464 |
| sortino_ratio | -0.5196 |
| max_drawdown | 0.4490 |
| cagr | -0.2113 |
| net_avg_win | 63.8399 |
| net_avg_loss | -94.2377 |
| avg_hold_time_bars | 4.6139 |
| exposure | 0.0543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

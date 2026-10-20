# EMA Hourly Continuation — DEXE/USDT P34_100

**Symbol:** DEXE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.6145 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9644 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -3.3295 |
| sortino_ratio | -1.0552 |
| max_drawdown | 0.7472 |
| cagr | -0.4028 |
| net_avg_win | 45.9285 |
| net_avg_loss | -71.6108 |
| avg_hold_time_bars | 18.7087 |
| exposure | 0.4380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

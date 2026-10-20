# EMA Hourly Continuation — AGLD/USDT P20_50

**Symbol:** AGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 999 |
| net_profit_factor | 0.4961 |
| net_win_rate | 0.4274 |
| gross_profit_factor | 0.8421 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -7.3004 |
| sortino_ratio | -3.2423 |
| max_drawdown | 0.9815 |
| cagr | -0.7905 |
| net_avg_win | 22.6056 |
| net_avg_loss | -34.0186 |
| avg_hold_time_bars | 5.6276 |
| exposure | 0.2544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

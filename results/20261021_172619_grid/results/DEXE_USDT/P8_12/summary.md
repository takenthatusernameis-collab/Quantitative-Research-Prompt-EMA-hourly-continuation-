# EMA Hourly Continuation — DEXE/USDT P8_12

**Symbol:** DEXE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.6479 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 0.9587 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -2.1434 |
| sortino_ratio | -0.5145 |
| max_drawdown | 0.4522 |
| cagr | -0.2104 |
| net_avg_win | 59.6713 |
| net_avg_loss | -89.5008 |
| avg_hold_time_bars | 11.9893 |
| exposure | 0.1526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — LQTY/USDT P100_144

**Symbol:** LQTY/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.6002 |
| net_win_rate | 0.4512 |
| gross_profit_factor | 0.8145 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -2.7559 |
| sortino_ratio | -0.6752 |
| max_drawdown | 0.5429 |
| cagr | -0.2663 |
| net_avg_win | 60.7371 |
| net_avg_loss | -83.1875 |
| avg_hold_time_bars | 5.9461 |
| exposure | 0.0799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

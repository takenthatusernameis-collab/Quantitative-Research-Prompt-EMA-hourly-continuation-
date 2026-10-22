# EMA Hourly Continuation — MAGIC/USDT P12_50

**Symbol:** MAGIC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.7828 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 1.0285 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -2.4899 |
| sortino_ratio | -0.9405 |
| max_drawdown | 0.7134 |
| cagr | -0.3511 |
| net_avg_win | 68.8248 |
| net_avg_loss | -87.1639 |
| avg_hold_time_bars | 11.2310 |
| exposure | 0.3558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

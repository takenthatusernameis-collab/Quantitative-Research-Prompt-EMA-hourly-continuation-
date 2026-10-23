# EMA Hourly Continuation — MAGIC/USDT P8_144

**Symbol:** MAGIC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.7301 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9878 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -2.2701 |
| sortino_ratio | -0.6960 |
| max_drawdown | 0.6093 |
| cagr | -0.2783 |
| net_avg_win | 66.0353 |
| net_avg_loss | -86.6660 |
| avg_hold_time_bars | 35.1709 |
| exposure | 0.7482 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

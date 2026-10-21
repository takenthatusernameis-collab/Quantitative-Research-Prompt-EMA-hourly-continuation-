# EMA Hourly Continuation — MAGIC/USDT P20_50

**Symbol:** MAGIC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.7864 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0736 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -2.2050 |
| sortino_ratio | -0.7823 |
| max_drawdown | 0.6431 |
| cagr | -0.3018 |
| net_avg_win | 70.1212 |
| net_avg_loss | -93.0470 |
| avg_hold_time_bars | 7.8462 |
| exposure | 0.2179 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

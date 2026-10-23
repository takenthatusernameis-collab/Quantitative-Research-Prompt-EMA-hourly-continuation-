# EMA Hourly Continuation — BOME/USDT P8_50

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1116 |
| net_profit_factor | 0.5746 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8605 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -5.7620 |
| sortino_ratio | -2.6832 |
| max_drawdown | 0.9684 |
| cagr | -0.7322 |
| net_avg_win | 25.2735 |
| net_avg_loss | -37.6878 |
| avg_hold_time_bars | 8.7016 |
| exposure | 0.4414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

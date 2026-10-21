# EMA Hourly Continuation — ALT/USDT P8_50

**Symbol:** ALT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.7064 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8767 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -3.3641 |
| sortino_ratio | -1.2786 |
| max_drawdown | 0.7937 |
| cagr | -0.4452 |
| net_avg_win | 56.6525 |
| net_avg_loss | -67.6209 |
| avg_hold_time_bars | 14.0767 |
| exposure | 0.4588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

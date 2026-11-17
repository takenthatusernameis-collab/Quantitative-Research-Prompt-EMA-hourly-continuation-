# EMA Hourly Continuation — NUM/USDT P8_50

**Symbol:** NUM/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1085 |
| net_profit_factor | 0.4331 |
| net_win_rate | 0.3687 |
| gross_profit_factor | 0.7489 |
| gross_win_rate | 0.3779 |
| sharpe_ratio | -9.9064 |
| sortino_ratio | -4.5687 |
| max_drawdown | 0.9967 |
| cagr | -0.8961 |
| net_avg_win | 19.0366 |
| net_avg_loss | -25.6653 |
| avg_hold_time_bars | 9.0691 |
| exposure | 0.4473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

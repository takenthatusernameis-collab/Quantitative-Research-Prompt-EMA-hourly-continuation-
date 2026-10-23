# EMA Hourly Continuation — NYM/USDT P8_21

**Symbol:** NYM/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1467 |
| net_profit_factor | 0.1784 |
| net_win_rate | 0.3108 |
| gross_profit_factor | 0.6004 |
| gross_win_rate | 0.3695 |
| sharpe_ratio | -18.6480 |
| sortino_ratio | -10.5593 |
| max_drawdown | 1.0000 |
| cagr | -0.9972 |
| net_avg_win | 4.7604 |
| net_avg_loss | -12.0383 |
| avg_hold_time_bars | 4.9877 |
| exposure | 0.3326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

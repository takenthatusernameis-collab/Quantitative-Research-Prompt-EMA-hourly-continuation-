# EMA Hourly Continuation — XDC/USDT P26_34

**Symbol:** XDC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1111 |
| net_profit_factor | 0.0753 |
| net_win_rate | 0.2997 |
| gross_profit_factor | 0.3540 |
| gross_win_rate | 0.4014 |
| sharpe_ratio | -16.9512 |
| sortino_ratio | -8.6012 |
| max_drawdown | 1.0000 |
| cagr | -0.9918 |
| net_avg_win | 2.4464 |
| net_avg_loss | -13.9005 |
| avg_hold_time_bars | 2.3546 |
| exposure | 0.1189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — NUM/USDT P21_100

**Symbol:** NUM/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.5021 |
| net_win_rate | 0.3855 |
| gross_profit_factor | 0.7108 |
| gross_win_rate | 0.3900 |
| sharpe_ratio | -6.2920 |
| sortino_ratio | -2.3036 |
| max_drawdown | 0.9373 |
| cagr | -0.6627 |
| net_avg_win | 36.1085 |
| net_avg_loss | -45.1236 |
| avg_hold_time_bars | 13.2304 |
| exposure | 0.4071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

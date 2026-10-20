# EMA Hourly Continuation — ALT/USDT P21_34

**Symbol:** ALT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.4366 |
| net_win_rate | 0.4364 |
| gross_profit_factor | 0.8551 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -8.0090 |
| sortino_ratio | -3.4930 |
| max_drawdown | 0.9870 |
| cagr | -0.8205 |
| net_avg_win | 18.4264 |
| net_avg_loss | -32.6738 |
| avg_hold_time_bars | 3.9874 |
| exposure | 0.1724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

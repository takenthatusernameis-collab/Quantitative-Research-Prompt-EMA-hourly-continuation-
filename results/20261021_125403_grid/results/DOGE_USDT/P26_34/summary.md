# EMA Hourly Continuation — DOGE/USDT P26_34

**Symbol:** DOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 163 |
| net_profit_factor | 0.6788 |
| net_win_rate | 0.5031 |
| gross_profit_factor | 0.9822 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -1.4219 |
| sortino_ratio | -0.2611 |
| max_drawdown | 0.2720 |
| cagr | -0.1123 |
| net_avg_win | 66.6396 |
| net_avg_loss | -99.3888 |
| avg_hold_time_bars | 5.1043 |
| exposure | 0.0378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

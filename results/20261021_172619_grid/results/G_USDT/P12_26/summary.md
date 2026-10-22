# EMA Hourly Continuation — G/USDT P12_26

**Symbol:** G/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.6168 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9523 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -3.9639 |
| sortino_ratio | -1.4921 |
| max_drawdown | 0.7740 |
| cagr | -0.4938 |
| net_avg_win | 42.9928 |
| net_avg_loss | -66.2637 |
| avg_hold_time_bars | 6.0270 |
| exposure | 0.1879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

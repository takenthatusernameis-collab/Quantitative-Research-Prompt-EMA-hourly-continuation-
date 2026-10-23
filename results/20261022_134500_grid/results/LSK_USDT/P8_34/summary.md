# EMA Hourly Continuation — LSK/USDT P8_34

**Symbol:** LSK/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1118 |
| net_profit_factor | 0.6098 |
| net_win_rate | 0.4633 |
| gross_profit_factor | 1.0801 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -6.7433 |
| sortino_ratio | -3.1768 |
| max_drawdown | 0.9798 |
| cagr | -0.7836 |
| net_avg_win | 29.5183 |
| net_avg_loss | -41.7940 |
| avg_hold_time_bars | 6.6216 |
| exposure | 0.3365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — UQC/USDT P144_200

**Symbol:** UQC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.2615 |
| net_win_rate | 0.2524 |
| gross_profit_factor | 0.5043 |
| gross_win_rate | 0.2952 |
| sharpe_ratio | -6.9729 |
| sortino_ratio | -1.4678 |
| max_drawdown | 0.8753 |
| cagr | -0.5620 |
| net_avg_win | 58.4909 |
| net_avg_loss | -75.4993 |
| avg_hold_time_bars | 20.2619 |
| exposure | 0.1926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — DEEP/USDT P12_50

**Symbol:** DEEP/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 762 |
| net_profit_factor | 0.7176 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 1.0110 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -3.9142 |
| sortino_ratio | -1.6968 |
| max_drawdown | 0.8273 |
| cagr | -0.5589 |
| net_avg_win | 54.8901 |
| net_avg_loss | -73.7326 |
| avg_hold_time_bars | 8.1811 |
| exposure | 0.3530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

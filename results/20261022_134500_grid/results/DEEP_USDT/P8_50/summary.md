# EMA Hourly Continuation — DEEP/USDT P8_50

**Symbol:** DEEP/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 819 |
| net_profit_factor | 0.7170 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9809 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -3.8340 |
| sortino_ratio | -1.7203 |
| max_drawdown | 0.8240 |
| cagr | -0.5635 |
| net_avg_win | 51.5652 |
| net_avg_loss | -68.3199 |
| avg_hold_time_bars | 9.9866 |
| exposure | 0.4631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

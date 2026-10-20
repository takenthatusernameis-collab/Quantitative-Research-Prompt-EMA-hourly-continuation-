# EMA Hourly Continuation — ORDI/USDT P8_50

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1127 |
| net_profit_factor | 0.6422 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.9721 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -5.7068 |
| sortino_ratio | -2.6867 |
| max_drawdown | 0.9619 |
| cagr | -0.7260 |
| net_avg_win | 32.4886 |
| net_avg_loss | -45.0739 |
| avg_hold_time_bars | 9.2591 |
| exposure | 0.4743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

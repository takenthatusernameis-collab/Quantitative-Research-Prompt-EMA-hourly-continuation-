# EMA Hourly Continuation — ORDI/USDT P12_20

**Symbol:** ORDI/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1566 |
| net_profit_factor | 0.3795 |
| net_win_rate | 0.4055 |
| gross_profit_factor | 0.8892 |
| gross_win_rate | 0.4330 |
| sharpe_ratio | -13.0407 |
| sortino_ratio | -7.3381 |
| max_drawdown | 0.9999 |
| cagr | -0.9761 |
| net_avg_win | 9.6297 |
| net_avg_loss | -17.3083 |
| avg_hold_time_bars | 2.1801 |
| exposure | 0.1552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

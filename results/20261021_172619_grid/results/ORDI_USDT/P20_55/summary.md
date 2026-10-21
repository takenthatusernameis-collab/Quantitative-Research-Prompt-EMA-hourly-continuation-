# EMA Hourly Continuation — ORDI/USDT P20_55

**Symbol:** ORDI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.6715 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.8515 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -2.8757 |
| sortino_ratio | -0.9265 |
| max_drawdown | 0.6639 |
| cagr | -0.3463 |
| net_avg_win | 56.8517 |
| net_avg_loss | -72.1272 |
| avg_hold_time_bars | 8.4561 |
| exposure | 0.1972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

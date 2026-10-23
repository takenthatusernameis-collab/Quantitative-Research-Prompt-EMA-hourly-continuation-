# EMA Hourly Continuation — AEVO/USDT P26_55

**Symbol:** AEVO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 944 |
| net_profit_factor | 0.5132 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.8846 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -6.6090 |
| sortino_ratio | -2.8602 |
| max_drawdown | 0.9715 |
| cagr | -0.7483 |
| net_avg_win | 24.0402 |
| net_avg_loss | -38.3601 |
| avg_hold_time_bars | 4.4852 |
| exposure | 0.1916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

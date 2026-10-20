# EMA Hourly Continuation — UQC/USDT P21_55

**Symbol:** UQC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.1519 |
| net_win_rate | 0.2711 |
| gross_profit_factor | 0.3864 |
| gross_win_rate | 0.2935 |
| sharpe_ratio | -8.7116 |
| sortino_ratio | -2.4806 |
| max_drawdown | 0.9636 |
| cagr | -0.7311 |
| net_avg_win | 15.8288 |
| net_avg_loss | -38.7749 |
| avg_hold_time_bars | 29.8532 |
| exposure | 0.5432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

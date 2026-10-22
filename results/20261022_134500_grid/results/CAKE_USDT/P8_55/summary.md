# EMA Hourly Continuation — CAKE/USDT P8_55

**Symbol:** CAKE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 956 |
| net_profit_factor | 0.5204 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.9619 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -6.0886 |
| sortino_ratio | -2.6345 |
| max_drawdown | 0.9622 |
| cagr | -0.7262 |
| net_avg_win | 23.3392 |
| net_avg_loss | -39.3834 |
| avg_hold_time_bars | 11.9655 |
| exposure | 0.5200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — AZERO/USDT P8_20

**Symbol:** AZERO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1470 |
| net_profit_factor | 0.3901 |
| net_win_rate | 0.4156 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -10.9366 |
| sortino_ratio | -5.8799 |
| max_drawdown | 0.9995 |
| cagr | -0.9488 |
| net_avg_win | 10.4643 |
| net_avg_loss | -19.0782 |
| avg_hold_time_bars | 3.5401 |
| exposure | 0.2355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

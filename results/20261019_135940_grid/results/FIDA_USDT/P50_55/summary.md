# EMA Hourly Continuation — FIDA/USDT P50_55

**Symbol:** FIDA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 801 |
| net_profit_factor | 0.2032 |
| net_win_rate | 0.3533 |
| gross_profit_factor | 0.7152 |
| gross_win_rate | 0.4145 |
| sharpe_ratio | -11.5581 |
| sortino_ratio | -4.7623 |
| max_drawdown | 0.9984 |
| cagr | -0.9202 |
| net_avg_win | 8.9940 |
| net_avg_loss | -24.1859 |
| avg_hold_time_bars | 2.4544 |
| exposure | 0.0890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

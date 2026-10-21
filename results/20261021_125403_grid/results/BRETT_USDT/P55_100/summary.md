# EMA Hourly Continuation — BRETT/USDT P55_100

**Symbol:** BRETT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.7894 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9552 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -1.3568 |
| sortino_ratio | -0.3565 |
| max_drawdown | 0.3237 |
| cagr | -0.1520 |
| net_avg_win | 77.7707 |
| net_avg_loss | -94.2879 |
| avg_hold_time_bars | 7.6520 |
| exposure | 0.1175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

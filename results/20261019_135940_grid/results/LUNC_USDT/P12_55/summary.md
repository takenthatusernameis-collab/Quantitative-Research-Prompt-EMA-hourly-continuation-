# EMA Hourly Continuation — LUNC/USDT P12_55

**Symbol:** LUNC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1099 |
| net_profit_factor | 0.4461 |
| net_win_rate | 0.4204 |
| gross_profit_factor | 0.8215 |
| gross_win_rate | 0.4359 |
| sharpe_ratio | -8.7518 |
| sortino_ratio | -4.0952 |
| max_drawdown | 0.9935 |
| cagr | -0.8636 |
| net_avg_win | 17.3178 |
| net_avg_loss | -28.1532 |
| avg_hold_time_bars | 6.9845 |
| exposure | 0.3489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — LUNA/USDT P34_55

**Symbol:** LUNA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1001 |
| net_profit_factor | 0.3445 |
| net_win_rate | 0.3986 |
| gross_profit_factor | 0.7758 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -10.7861 |
| sortino_ratio | -4.8672 |
| max_drawdown | 0.9982 |
| cagr | -0.9184 |
| net_avg_win | 13.1497 |
| net_avg_loss | -25.2960 |
| avg_hold_time_bars | 2.8282 |
| exposure | 0.1287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

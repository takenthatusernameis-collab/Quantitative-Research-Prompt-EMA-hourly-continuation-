# EMA Hourly Continuation — POPCAT/USDT P55_200

**Symbol:** POPCAT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.6955 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.9061 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -2.2882 |
| sortino_ratio | -0.6347 |
| max_drawdown | 0.5043 |
| cagr | -0.2604 |
| net_avg_win | 69.2226 |
| net_avg_loss | -88.8441 |
| avg_hold_time_bars | 22.1552 |
| exposure | 0.3921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

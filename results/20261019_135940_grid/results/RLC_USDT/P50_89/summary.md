# EMA Hourly Continuation — RLC/USDT P50_89

**Symbol:** RLC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.5100 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.9177 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -5.4710 |
| sortino_ratio | -2.0214 |
| max_drawdown | 0.9244 |
| cagr | -0.6279 |
| net_avg_win | 29.5309 |
| net_avg_loss | -51.3820 |
| avg_hold_time_bars | 5.1499 |
| exposure | 0.1608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

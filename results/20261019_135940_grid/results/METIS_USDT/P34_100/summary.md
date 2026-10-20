# EMA Hourly Continuation — METIS/USDT P34_100

**Symbol:** METIS/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.5107 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.8224 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -5.6450 |
| sortino_ratio | -2.0737 |
| max_drawdown | 0.9215 |
| cagr | -0.6344 |
| net_avg_win | 32.4489 |
| net_avg_loss | -48.4684 |
| avg_hold_time_bars | 8.6023 |
| exposure | 0.2675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

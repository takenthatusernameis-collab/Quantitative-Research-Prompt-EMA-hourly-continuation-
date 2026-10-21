# EMA Hourly Continuation — CARV/USDT P20_21

**Symbol:** CARV/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 196 |
| net_profit_factor | 0.6600 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0386 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -2.0961 |
| sortino_ratio | -0.4686 |
| max_drawdown | 0.3837 |
| cagr | -0.1942 |
| net_avg_win | 69.5573 |
| net_avg_loss | -107.5596 |
| avg_hold_time_bars | 6.3776 |
| exposure | 0.0703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

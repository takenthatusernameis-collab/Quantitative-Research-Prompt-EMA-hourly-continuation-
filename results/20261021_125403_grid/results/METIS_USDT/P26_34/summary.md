# EMA Hourly Continuation — METIS/USDT P26_34

**Symbol:** METIS/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.5988 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8630 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -2.4217 |
| sortino_ratio | -0.5219 |
| max_drawdown | 0.4654 |
| cagr | -0.2126 |
| net_avg_win | 64.1454 |
| net_avg_loss | -92.2020 |
| avg_hold_time_bars | 4.6167 |
| exposure | 0.0476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — POLYX/USDT P8_89

**Symbol:** POLYX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.7243 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 1.0370 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -3.1458 |
| sortino_ratio | -1.1540 |
| max_drawdown | 0.7887 |
| cagr | -0.4241 |
| net_avg_win | 59.1704 |
| net_avg_loss | -78.6208 |
| avg_hold_time_bars | 20.5920 |
| exposure | 0.6355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

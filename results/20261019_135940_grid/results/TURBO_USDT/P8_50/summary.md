# EMA Hourly Continuation — TURBO/USDT P8_50

**Symbol:** TURBO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.6559 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9792 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -5.0807 |
| sortino_ratio | -2.3896 |
| max_drawdown | 0.9175 |
| cagr | -0.6838 |
| net_avg_win | 38.2896 |
| net_avg_loss | -54.3051 |
| avg_hold_time_bars | 8.5404 |
| exposure | 0.4379 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

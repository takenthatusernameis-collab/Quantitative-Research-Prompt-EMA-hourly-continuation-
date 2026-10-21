# EMA Hourly Continuation — ELON/USDT P26_100

**Symbol:** ELON/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.7026 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.8962 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -2.3838 |
| sortino_ratio | -0.7037 |
| max_drawdown | 0.5830 |
| cagr | -0.2757 |
| net_avg_win | 64.9457 |
| net_avg_loss | -82.2514 |
| avg_hold_time_bars | 14.7366 |
| exposure | 0.2874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

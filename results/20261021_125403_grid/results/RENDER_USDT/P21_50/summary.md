# EMA Hourly Continuation — RENDER/USDT P21_50

**Symbol:** RENDER/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.7522 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 0.9838 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -1.8935 |
| sortino_ratio | -0.5819 |
| max_drawdown | 0.4914 |
| cagr | -0.2345 |
| net_avg_win | 67.2862 |
| net_avg_loss | -89.0048 |
| avg_hold_time_bars | 6.6977 |
| exposure | 0.1403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

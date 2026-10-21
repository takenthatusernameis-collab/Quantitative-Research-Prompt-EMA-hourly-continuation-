# EMA Hourly Continuation — ORBS/USDT P8_21

**Symbol:** ORBS/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.5384 |
| net_win_rate | 0.4135 |
| gross_profit_factor | 0.8602 |
| gross_win_rate | 0.4135 |
| sharpe_ratio | -6.4942 |
| sortino_ratio | -2.3986 |
| max_drawdown | 0.9390 |
| cagr | -0.6717 |
| net_avg_win | 39.8231 |
| net_avg_loss | -52.1573 |
| avg_hold_time_bars | 7.9534 |
| exposure | 0.2404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

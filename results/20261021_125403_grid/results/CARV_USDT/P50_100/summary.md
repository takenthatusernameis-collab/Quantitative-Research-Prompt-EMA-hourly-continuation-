# EMA Hourly Continuation — CARV/USDT P50_100

**Symbol:** CARV/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.5446 |
| net_win_rate | 0.4333 |
| gross_profit_factor | 0.7439 |
| gross_win_rate | 0.4333 |
| sharpe_ratio | -3.3101 |
| sortino_ratio | -0.8600 |
| max_drawdown | 0.5706 |
| cagr | -0.3265 |
| net_avg_win | 56.3727 |
| net_avg_loss | -79.1508 |
| avg_hold_time_bars | 8.9185 |
| exposure | 0.1355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

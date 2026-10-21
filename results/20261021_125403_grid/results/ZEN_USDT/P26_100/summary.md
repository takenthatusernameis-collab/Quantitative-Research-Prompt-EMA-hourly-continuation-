# EMA Hourly Continuation — ZEN/USDT P26_100

**Symbol:** ZEN/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.7424 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9278 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -1.9687 |
| sortino_ratio | -0.6082 |
| max_drawdown | 0.5293 |
| cagr | -0.2452 |
| net_avg_win | 64.3109 |
| net_avg_loss | -81.2595 |
| avg_hold_time_bars | 15.7079 |
| exposure | 0.3349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CAKE/USDT P20_50

**Symbol:** CAKE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6338 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.8951 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -3.0128 |
| sortino_ratio | -0.9575 |
| max_drawdown | 0.6768 |
| cagr | -0.3556 |
| net_avg_win | 49.0065 |
| net_avg_loss | -71.0070 |
| avg_hold_time_bars | 9.1826 |
| exposure | 0.2058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

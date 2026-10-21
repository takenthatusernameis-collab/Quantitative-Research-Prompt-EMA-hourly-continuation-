# EMA Hourly Continuation — ZRX/USDT P89_100

**Symbol:** ZRX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 191 |
| net_profit_factor | 0.5285 |
| net_win_rate | 0.4555 |
| gross_profit_factor | 0.8463 |
| gross_win_rate | 0.4555 |
| sharpe_ratio | -2.7674 |
| sortino_ratio | -0.5489 |
| max_drawdown | 0.4695 |
| cagr | -0.2231 |
| net_avg_win | 60.5029 |
| net_avg_loss | -95.7602 |
| avg_hold_time_bars | 5.0471 |
| exposure | 0.0438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

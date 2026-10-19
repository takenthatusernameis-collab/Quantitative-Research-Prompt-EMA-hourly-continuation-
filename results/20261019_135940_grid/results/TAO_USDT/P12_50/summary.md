# EMA Hourly Continuation — TAO/USDT P12_50

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1103 |
| net_profit_factor | 0.6273 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.9462 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -5.9094 |
| sortino_ratio | -2.7599 |
| max_drawdown | 0.9659 |
| cagr | -0.7355 |
| net_avg_win | 31.4070 |
| net_avg_loss | -44.1686 |
| avg_hold_time_bars | 6.5666 |
| exposure | 0.3292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

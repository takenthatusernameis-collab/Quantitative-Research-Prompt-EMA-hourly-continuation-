# EMA Hourly Continuation — ZRO/USDT P26_50

**Symbol:** ZRO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 928 |
| net_profit_factor | 0.6039 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 1.0296 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -5.6705 |
| sortino_ratio | -2.5164 |
| max_drawdown | 0.9446 |
| cagr | -0.7061 |
| net_avg_win | 32.0756 |
| net_avg_loss | -49.5729 |
| avg_hold_time_bars | 3.7748 |
| exposure | 0.1715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

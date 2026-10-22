# EMA Hourly Continuation — SOL/USDT P8_100

**Symbol:** SOL/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.5652 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.9134 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -4.9380 |
| sortino_ratio | -1.7869 |
| max_drawdown | 0.8994 |
| cagr | -0.5843 |
| net_avg_win | 37.4288 |
| net_avg_loss | -56.9982 |
| avg_hold_time_bars | 20.8817 |
| exposure | 0.6340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

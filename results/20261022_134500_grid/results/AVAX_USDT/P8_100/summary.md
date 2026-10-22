# EMA Hourly Continuation — AVAX/USDT P8_100

**Symbol:** AVAX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.6435 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.9542 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -4.4208 |
| sortino_ratio | -1.6179 |
| max_drawdown | 0.8666 |
| cagr | -0.5400 |
| net_avg_win | 48.9993 |
| net_avg_loss | -66.1028 |
| avg_hold_time_bars | 20.7868 |
| exposure | 0.6425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

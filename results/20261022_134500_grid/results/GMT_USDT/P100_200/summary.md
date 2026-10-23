# EMA Hourly Continuation — GMT/USDT P100_200

**Symbol:** GMT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.6610 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 0.9962 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -2.6195 |
| sortino_ratio | -0.7388 |
| max_drawdown | 0.5986 |
| cagr | -0.2946 |
| net_avg_win | 57.7767 |
| net_avg_loss | -86.0952 |
| avg_hold_time_bars | 8.9572 |
| exposure | 0.1616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

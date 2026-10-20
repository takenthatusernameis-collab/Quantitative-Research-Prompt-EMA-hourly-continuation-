# EMA Hourly Continuation — XEC/USDT P21_50

**Symbol:** XEC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1059 |
| net_profit_factor | 0.4950 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 1.0061 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -8.2737 |
| sortino_ratio | -3.8167 |
| max_drawdown | 0.9909 |
| cagr | -0.8446 |
| net_avg_win | 20.6189 |
| net_avg_loss | -33.3679 |
| avg_hold_time_bars | 5.0897 |
| exposure | 0.2439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

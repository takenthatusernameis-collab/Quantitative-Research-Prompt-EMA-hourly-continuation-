# EMA Hourly Continuation — AXS/USDT P34_100

**Symbol:** AXS/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.8458 |
| net_win_rate | 0.5230 |
| gross_profit_factor | 1.0906 |
| gross_win_rate | 0.5255 |
| sharpe_ratio | -0.9844 |
| sortino_ratio | -0.2801 |
| max_drawdown | 0.3063 |
| cagr | -0.1224 |
| net_avg_win | 75.0629 |
| net_avg_loss | -97.2896 |
| avg_hold_time_bars | 15.1250 |
| exposure | 0.2683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

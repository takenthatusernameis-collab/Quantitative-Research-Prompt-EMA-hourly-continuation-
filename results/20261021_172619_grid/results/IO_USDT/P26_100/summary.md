# EMA Hourly Continuation — IO/USDT P26_100

**Symbol:** IO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.8247 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9800 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -1.2787 |
| sortino_ratio | -0.3966 |
| max_drawdown | 0.3905 |
| cagr | -0.1685 |
| net_avg_win | 75.8116 |
| net_avg_loss | -90.6811 |
| avg_hold_time_bars | 13.9229 |
| exposure | 0.2973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

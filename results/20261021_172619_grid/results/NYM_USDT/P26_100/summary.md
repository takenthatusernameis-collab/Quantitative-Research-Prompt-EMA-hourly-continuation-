# EMA Hourly Continuation — NYM/USDT P26_100

**Symbol:** NYM/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.4563 |
| net_win_rate | 0.4162 |
| gross_profit_factor | 0.6933 |
| gross_win_rate | 0.4191 |
| sharpe_ratio | -4.0882 |
| sortino_ratio | -1.0785 |
| max_drawdown | 0.7261 |
| cagr | -0.3956 |
| net_avg_win | 41.8253 |
| net_avg_loss | -65.3429 |
| avg_hold_time_bars | 21.4104 |
| exposure | 0.3367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

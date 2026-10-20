# EMA Hourly Continuation — KSM/USDT P26_55

**Symbol:** KSM/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 878 |
| net_profit_factor | 0.4935 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8968 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -6.9644 |
| sortino_ratio | -2.9227 |
| max_drawdown | 0.9729 |
| cagr | -0.7591 |
| net_avg_win | 23.6171 |
| net_avg_loss | -40.2310 |
| avg_hold_time_bars | 4.8599 |
| exposure | 0.1940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

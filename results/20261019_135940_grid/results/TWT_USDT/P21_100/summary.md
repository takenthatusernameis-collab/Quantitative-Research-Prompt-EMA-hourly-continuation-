# EMA Hourly Continuation — TWT/USDT P21_100

**Symbol:** TWT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.5544 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.9552 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -5.0358 |
| sortino_ratio | -1.9145 |
| max_drawdown | 0.9145 |
| cagr | -0.6093 |
| net_avg_win | 32.2874 |
| net_avg_loss | -52.5175 |
| avg_hold_time_bars | 11.7962 |
| exposure | 0.3946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

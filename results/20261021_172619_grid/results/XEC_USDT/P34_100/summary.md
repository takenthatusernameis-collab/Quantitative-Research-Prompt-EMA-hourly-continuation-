# EMA Hourly Continuation — XEC/USDT P34_100

**Symbol:** XEC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.6763 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9277 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -2.9351 |
| sortino_ratio | -0.9712 |
| max_drawdown | 0.6961 |
| cagr | -0.3596 |
| net_avg_win | 54.6777 |
| net_avg_loss | -74.4907 |
| avg_hold_time_bars | 11.3829 |
| exposure | 0.2771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

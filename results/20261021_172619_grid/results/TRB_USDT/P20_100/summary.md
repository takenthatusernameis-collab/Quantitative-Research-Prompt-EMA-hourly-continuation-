# EMA Hourly Continuation — TRB/USDT P20_100

**Symbol:** TRB/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.6775 |
| net_win_rate | 0.4584 |
| gross_profit_factor | 0.8417 |
| gross_win_rate | 0.4584 |
| sharpe_ratio | -2.5310 |
| sortino_ratio | -0.7360 |
| max_drawdown | 0.5879 |
| cagr | -0.2869 |
| net_avg_win | 62.4828 |
| net_avg_loss | -78.0631 |
| avg_hold_time_bars | 23.3135 |
| exposure | 0.4441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

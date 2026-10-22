# EMA Hourly Continuation — ZEC/USDT P12_21

**Symbol:** ZEC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1454 |
| net_profit_factor | 0.2133 |
| net_win_rate | 0.4243 |
| gross_profit_factor | 0.6174 |
| gross_win_rate | 0.4450 |
| sharpe_ratio | -11.5413 |
| sortino_ratio | -6.2226 |
| max_drawdown | 0.9997 |
| cagr | -0.9582 |
| net_avg_win | 4.3917 |
| net_avg_loss | -15.1807 |
| avg_hold_time_bars | 2.1891 |
| exposure | 0.1447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CFX/USDT P12_89

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 587 |
| net_profit_factor | 0.6560 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9538 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -3.3754 |
| sortino_ratio | -1.1537 |
| max_drawdown | 0.7571 |
| cagr | -0.4214 |
| net_avg_win | 50.1570 |
| net_avg_loss | -71.6619 |
| avg_hold_time_bars | 22.2845 |
| exposure | 0.5946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

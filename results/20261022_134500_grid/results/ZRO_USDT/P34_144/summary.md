# EMA Hourly Continuation — ZRO/USDT P34_144

**Symbol:** ZRO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.6659 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.8987 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -2.9137 |
| sortino_ratio | -0.9400 |
| max_drawdown | 0.6640 |
| cagr | -0.3607 |
| net_avg_win | 55.8952 |
| net_avg_loss | -75.4422 |
| avg_hold_time_bars | 15.9570 |
| exposure | 0.3811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

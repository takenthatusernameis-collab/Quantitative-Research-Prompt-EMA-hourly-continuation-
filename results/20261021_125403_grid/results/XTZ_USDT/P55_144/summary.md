# EMA Hourly Continuation — XTZ/USDT P55_144

**Symbol:** XTZ/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7864 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0538 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -1.4049 |
| sortino_ratio | -0.3779 |
| max_drawdown | 0.4046 |
| cagr | -0.1592 |
| net_avg_win | 72.6108 |
| net_avg_loss | -96.6510 |
| avg_hold_time_bars | 17.3114 |
| exposure | 0.2754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

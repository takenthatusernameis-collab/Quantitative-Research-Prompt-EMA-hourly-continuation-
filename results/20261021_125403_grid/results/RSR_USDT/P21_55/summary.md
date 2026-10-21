# EMA Hourly Continuation — RSR/USDT P21_55

**Symbol:** RSR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.7800 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9860 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -1.7351 |
| sortino_ratio | -0.5526 |
| max_drawdown | 0.5227 |
| cagr | -0.2250 |
| net_avg_win | 68.1526 |
| net_avg_loss | -86.6657 |
| avg_hold_time_bars | 9.2611 |
| exposure | 0.2080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

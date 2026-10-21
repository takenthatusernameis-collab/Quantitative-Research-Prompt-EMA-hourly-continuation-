# EMA Hourly Continuation — KCS/USDT P26_50

**Symbol:** KCS/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.3200 |
| net_win_rate | 0.3727 |
| gross_profit_factor | 0.6580 |
| gross_win_rate | 0.3780 |
| sharpe_ratio | -6.7410 |
| sortino_ratio | -1.9041 |
| max_drawdown | 0.8951 |
| cagr | -0.5905 |
| net_avg_win | 30.2569 |
| net_avg_loss | -56.1675 |
| avg_hold_time_bars | 6.8820 |
| exposure | 0.1167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

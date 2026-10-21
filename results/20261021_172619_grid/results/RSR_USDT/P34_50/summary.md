# EMA Hourly Continuation — RSR/USDT P34_50

**Symbol:** RSR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.8336 |
| net_win_rate | 0.5267 |
| gross_profit_factor | 1.1083 |
| gross_win_rate | 0.5267 |
| sharpe_ratio | -0.9132 |
| sortino_ratio | -0.2134 |
| max_drawdown | 0.2696 |
| cagr | -0.0940 |
| net_avg_win | 79.7135 |
| net_avg_loss | -106.4158 |
| avg_hold_time_bars | 5.1603 |
| exposure | 0.0615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

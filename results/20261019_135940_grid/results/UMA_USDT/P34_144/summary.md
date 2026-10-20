# EMA Hourly Continuation — UMA/USDT P34_144

**Symbol:** UMA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.6453 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9475 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -2.8772 |
| sortino_ratio | -0.9173 |
| max_drawdown | 0.6742 |
| cagr | -0.3490 |
| net_avg_win | 48.6028 |
| net_avg_loss | -72.1030 |
| avg_hold_time_bars | 17.9347 |
| exposure | 0.4117 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

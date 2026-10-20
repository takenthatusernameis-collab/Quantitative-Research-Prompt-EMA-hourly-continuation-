# EMA Hourly Continuation — AMP/USDT P89_100

**Symbol:** AMP/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 824 |
| net_profit_factor | 0.1423 |
| net_win_rate | 0.2888 |
| gross_profit_factor | 0.5835 |
| gross_win_rate | 0.3544 |
| sharpe_ratio | -14.1065 |
| sortino_ratio | -6.0762 |
| max_drawdown | 0.9997 |
| cagr | -0.9620 |
| net_avg_win | 6.9677 |
| net_avg_loss | -19.8901 |
| avg_hold_time_bars | 2.1748 |
| exposure | 0.0815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

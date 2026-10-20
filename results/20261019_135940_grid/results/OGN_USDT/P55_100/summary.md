# EMA Hourly Continuation — OGN/USDT P55_100

**Symbol:** OGN/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.3955 |
| net_win_rate | 0.4136 |
| gross_profit_factor | 0.7162 |
| gross_win_rate | 0.4306 |
| sharpe_ratio | -6.9049 |
| sortino_ratio | -2.4806 |
| max_drawdown | 0.9538 |
| cagr | -0.7026 |
| net_avg_win | 23.2645 |
| net_avg_loss | -41.4885 |
| avg_hold_time_bars | 6.0849 |
| exposure | 0.1784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

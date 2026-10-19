# EMA Hourly Continuation — FIL/USDT P20_50

**Symbol:** FIL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.4179 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.7981 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -7.6115 |
| sortino_ratio | -3.3889 |
| max_drawdown | 0.9854 |
| cagr | -0.8129 |
| net_avg_win | 15.5419 |
| net_avg_loss | -30.7691 |
| avg_hold_time_bars | 4.2080 |
| exposure | 0.1922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

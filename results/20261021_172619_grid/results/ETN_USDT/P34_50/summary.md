# EMA Hourly Continuation — ETN/USDT P34_50

**Symbol:** ETN/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 203 |
| net_profit_factor | 0.5003 |
| net_win_rate | 0.4089 |
| gross_profit_factor | 0.6765 |
| gross_win_rate | 0.4089 |
| sharpe_ratio | -3.2485 |
| sortino_ratio | -0.7172 |
| max_drawdown | 0.5059 |
| cagr | -0.2817 |
| net_avg_win | 60.4390 |
| net_avg_loss | -83.5587 |
| avg_hold_time_bars | 6.2512 |
| exposure | 0.0689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

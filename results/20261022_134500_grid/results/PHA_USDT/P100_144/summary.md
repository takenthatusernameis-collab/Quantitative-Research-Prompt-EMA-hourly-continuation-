# EMA Hourly Continuation — PHA/USDT P100_144

**Symbol:** PHA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.3817 |
| net_win_rate | 0.4251 |
| gross_profit_factor | 0.6968 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -5.4854 |
| sortino_ratio | -1.7301 |
| max_drawdown | 0.8882 |
| cagr | -0.5711 |
| net_avg_win | 25.5238 |
| net_avg_loss | -49.4555 |
| avg_hold_time_bars | 4.0539 |
| exposure | 0.0923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

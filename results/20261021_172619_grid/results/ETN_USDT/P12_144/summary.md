# EMA Hourly Continuation — ETN/USDT P12_144

**Symbol:** ETN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6211 |
| net_win_rate | 0.4296 |
| gross_profit_factor | 0.7490 |
| gross_win_rate | 0.4296 |
| sharpe_ratio | -3.3140 |
| sortino_ratio | -1.0380 |
| max_drawdown | 0.6512 |
| cagr | -0.3809 |
| net_avg_win | 58.7913 |
| net_avg_loss | -71.2978 |
| avg_hold_time_bars | 23.3228 |
| exposure | 0.5219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

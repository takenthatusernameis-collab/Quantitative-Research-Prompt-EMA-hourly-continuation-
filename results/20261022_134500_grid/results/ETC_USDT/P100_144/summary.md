# EMA Hourly Continuation — ETC/USDT P100_144

**Symbol:** ETC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.3987 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.9225 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -6.4682 |
| sortino_ratio | -2.0786 |
| max_drawdown | 0.9298 |
| cagr | -0.6516 |
| net_avg_win | 26.9103 |
| net_avg_loss | -54.2268 |
| avg_hold_time_bars | 3.6265 |
| exposure | 0.0847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

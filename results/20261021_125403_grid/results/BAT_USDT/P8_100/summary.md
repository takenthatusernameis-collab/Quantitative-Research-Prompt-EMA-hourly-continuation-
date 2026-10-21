# EMA Hourly Continuation — BAT/USDT P8_100

**Symbol:** BAT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.7959 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.0089 |
| gross_win_rate | 0.5020 |
| sharpe_ratio | -1.6283 |
| sortino_ratio | -0.5262 |
| max_drawdown | 0.4967 |
| cagr | -0.2155 |
| net_avg_win | 69.5021 |
| net_avg_loss | -88.0142 |
| avg_hold_time_bars | 28.7314 |
| exposure | 0.6660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

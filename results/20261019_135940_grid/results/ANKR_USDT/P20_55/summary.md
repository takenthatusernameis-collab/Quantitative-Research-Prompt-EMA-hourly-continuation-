# EMA Hourly Continuation — ANKR/USDT P20_55

**Symbol:** ANKR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 975 |
| net_profit_factor | 0.5389 |
| net_win_rate | 0.4256 |
| gross_profit_factor | 0.9331 |
| gross_win_rate | 0.4431 |
| sharpe_ratio | -8.1889 |
| sortino_ratio | -3.5986 |
| max_drawdown | 0.9890 |
| cagr | -0.8317 |
| net_avg_win | 27.8444 |
| net_avg_loss | -38.2885 |
| avg_hold_time_bars | 6.2072 |
| exposure | 0.2751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

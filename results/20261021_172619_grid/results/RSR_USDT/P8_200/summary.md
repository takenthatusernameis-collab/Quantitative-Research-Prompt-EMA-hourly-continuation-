# EMA Hourly Continuation — RSR/USDT P8_200

**Symbol:** RSR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.8050 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9276 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -1.0087 |
| sortino_ratio | -0.2170 |
| max_drawdown | 0.2809 |
| cagr | -0.0962 |
| net_avg_win | 84.1594 |
| net_avg_loss | -97.4608 |
| avg_hold_time_bars | 79.6579 |
| exposure | 0.8255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

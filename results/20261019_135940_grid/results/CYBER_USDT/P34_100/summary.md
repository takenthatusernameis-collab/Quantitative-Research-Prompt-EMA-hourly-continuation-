# EMA Hourly Continuation — CYBER/USDT P34_100

**Symbol:** CYBER/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.6769 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0070 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -2.9489 |
| sortino_ratio | -1.0440 |
| max_drawdown | 0.7268 |
| cagr | -0.3847 |
| net_avg_win | 47.3144 |
| net_avg_loss | -71.5048 |
| avg_hold_time_bars | 9.8136 |
| exposure | 0.2752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

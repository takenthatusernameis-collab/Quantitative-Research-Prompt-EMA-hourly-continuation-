# EMA Hourly Continuation — MANA/USDT P26_200

**Symbol:** MANA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.7493 |
| net_win_rate | 0.5220 |
| gross_profit_factor | 1.1183 |
| gross_win_rate | 0.5275 |
| sharpe_ratio | -1.7925 |
| sortino_ratio | -0.4812 |
| max_drawdown | 0.4761 |
| cagr | -0.2067 |
| net_avg_win | 69.3430 |
| net_avg_loss | -101.0582 |
| avg_hold_time_bars | 36.6896 |
| exposure | 0.6070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CGPT/USDT P26_200

**Symbol:** CGPT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.8641 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0087 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -0.7593 |
| sortino_ratio | -0.1884 |
| max_drawdown | 0.2108 |
| cagr | -0.0854 |
| net_avg_win | 84.5144 |
| net_avg_loss | -99.1205 |
| avg_hold_time_bars | 39.8367 |
| exposure | 0.5432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

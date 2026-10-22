# EMA Hourly Continuation — FLUX/USDT P55_100

**Symbol:** FLUX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.7876 |
| net_win_rate | 0.5183 |
| gross_profit_factor | 1.0506 |
| gross_win_rate | 0.5183 |
| sharpe_ratio | -1.2759 |
| sortino_ratio | -0.3462 |
| max_drawdown | 0.3568 |
| cagr | -0.1479 |
| net_avg_win | 66.6933 |
| net_avg_loss | -91.1149 |
| avg_hold_time_bars | 8.2873 |
| exposure | 0.1337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

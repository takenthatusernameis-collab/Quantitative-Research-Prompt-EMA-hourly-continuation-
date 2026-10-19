# EMA Hourly Continuation — AVAX/USDT P55_200

**Symbol:** AVAX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.5496 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8513 |
| gross_win_rate | 0.4553 |
| sharpe_ratio | -3.8670 |
| sortino_ratio | -1.0405 |
| max_drawdown | 0.7274 |
| cagr | -0.3979 |
| net_avg_win | 53.6025 |
| net_avg_loss | -78.0173 |
| avg_hold_time_bars | 19.8022 |
| exposure | 0.3321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

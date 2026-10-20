# EMA Hourly Continuation — MOVR/USDT P50_100

**Symbol:** MOVR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.4472 |
| net_win_rate | 0.4237 |
| gross_profit_factor | 0.7540 |
| gross_win_rate | 0.4299 |
| sharpe_ratio | -6.1017 |
| sortino_ratio | -2.1982 |
| max_drawdown | 0.9342 |
| cagr | -0.6503 |
| net_avg_win | 27.3136 |
| net_avg_loss | -44.9102 |
| avg_hold_time_bars | 5.9045 |
| exposure | 0.1742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — LISTA/USDT P100_200

**Symbol:** LISTA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.7498 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 0.9450 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -1.5156 |
| sortino_ratio | -0.3796 |
| max_drawdown | 0.3551 |
| cagr | -0.1613 |
| net_avg_win | 72.0734 |
| net_avg_loss | -92.1748 |
| avg_hold_time_bars | 11.3427 |
| exposure | 0.1586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

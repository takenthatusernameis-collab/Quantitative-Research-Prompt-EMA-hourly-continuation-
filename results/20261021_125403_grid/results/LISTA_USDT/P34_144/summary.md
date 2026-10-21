# EMA Hourly Continuation — LISTA/USDT P34_144

**Symbol:** LISTA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7862 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9536 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -1.4870 |
| sortino_ratio | -0.4101 |
| max_drawdown | 0.3650 |
| cagr | -0.1734 |
| net_avg_win | 77.6139 |
| net_avg_loss | -94.2860 |
| avg_hold_time_bars | 22.8908 |
| exposure | 0.3895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

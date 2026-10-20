# EMA Hourly Continuation — ORDI/USDT P50_144

**Symbol:** ORDI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6128 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.8729 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -3.3275 |
| sortino_ratio | -1.0369 |
| max_drawdown | 0.7139 |
| cagr | -0.3876 |
| net_avg_win | 49.1603 |
| net_avg_loss | -69.0189 |
| avg_hold_time_bars | 13.0892 |
| exposure | 0.2933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

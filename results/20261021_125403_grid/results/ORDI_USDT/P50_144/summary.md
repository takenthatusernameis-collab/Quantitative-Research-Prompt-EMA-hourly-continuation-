# EMA Hourly Continuation — ORDI/USDT P50_144

**Symbol:** ORDI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7006 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8594 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -2.0782 |
| sortino_ratio | -0.5572 |
| max_drawdown | 0.4950 |
| cagr | -0.2259 |
| net_avg_win | 67.2610 |
| net_avg_loss | -82.9373 |
| avg_hold_time_bars | 17.3174 |
| exposure | 0.2802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

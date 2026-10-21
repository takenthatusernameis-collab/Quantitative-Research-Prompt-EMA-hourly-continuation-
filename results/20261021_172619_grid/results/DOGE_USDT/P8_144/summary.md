# EMA Hourly Continuation — DOGE/USDT P8_144

**Symbol:** DOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7604 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9359 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -1.5819 |
| sortino_ratio | -0.4178 |
| max_drawdown | 0.4254 |
| cagr | -0.1758 |
| net_avg_win | 73.5524 |
| net_avg_loss | -90.7126 |
| avg_hold_time_bars | 46.8484 |
| exposure | 0.7304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — MERL/USDT P20_144

**Symbol:** MERL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7304 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.9429 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -2.6551 |
| sortino_ratio | -0.8177 |
| max_drawdown | 0.6864 |
| cagr | -0.3194 |
| net_avg_win | 75.4786 |
| net_avg_loss | -90.3204 |
| avg_hold_time_bars | 25.8761 |
| exposure | 0.5614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

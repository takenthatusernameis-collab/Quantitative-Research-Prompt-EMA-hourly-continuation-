# EMA Hourly Continuation — ORBS/USDT P8_144

**Symbol:** ORBS/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.7150 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.9164 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -2.5711 |
| sortino_ratio | -0.7806 |
| max_drawdown | 0.6154 |
| cagr | -0.3019 |
| net_avg_win | 69.6726 |
| net_avg_loss | -85.8184 |
| avg_hold_time_bars | 33.9912 |
| exposure | 0.7061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

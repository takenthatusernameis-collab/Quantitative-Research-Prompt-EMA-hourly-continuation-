# EMA Hourly Continuation — POLYX/USDT P55_144

**Symbol:** POLYX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.6578 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9875 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -2.9612 |
| sortino_ratio | -0.9075 |
| max_drawdown | 0.6660 |
| cagr | -0.3483 |
| net_avg_win | 55.0529 |
| net_avg_loss | -80.8836 |
| avg_hold_time_bars | 12.1261 |
| exposure | 0.2580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

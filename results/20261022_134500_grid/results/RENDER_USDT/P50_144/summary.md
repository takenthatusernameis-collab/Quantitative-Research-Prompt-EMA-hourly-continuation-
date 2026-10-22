# EMA Hourly Continuation — RENDER/USDT P50_144

**Symbol:** RENDER/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.6794 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9638 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -2.6330 |
| sortino_ratio | -0.8324 |
| max_drawdown | 0.5966 |
| cagr | -0.3240 |
| net_avg_win | 57.1118 |
| net_avg_loss | -81.7441 |
| avg_hold_time_bars | 11.9465 |
| exposure | 0.2711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

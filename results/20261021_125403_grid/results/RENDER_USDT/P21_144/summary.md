# EMA Hourly Continuation — RENDER/USDT P21_144

**Symbol:** RENDER/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.8680 |
| net_win_rate | 0.5078 |
| gross_profit_factor | 1.0238 |
| gross_win_rate | 0.5078 |
| sharpe_ratio | -0.8615 |
| sortino_ratio | -0.2374 |
| max_drawdown | 0.2986 |
| cagr | -0.1063 |
| net_avg_win | 87.5707 |
| net_avg_loss | -104.0998 |
| avg_hold_time_bars | 30.5266 |
| exposure | 0.5140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — RENDER/USDT P89_144

**Symbol:** RENDER/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.9310 |
| net_win_rate | 0.5489 |
| gross_profit_factor | 1.2115 |
| gross_win_rate | 0.5489 |
| sharpe_ratio | -0.3566 |
| sortino_ratio | -0.0855 |
| max_drawdown | 0.2512 |
| cagr | -0.0418 |
| net_avg_win | 92.3691 |
| net_avg_loss | -120.7379 |
| avg_hold_time_bars | 8.2128 |
| exposure | 0.1019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — BLUR/USDT P50_144

**Symbol:** BLUR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.7364 |
| net_win_rate | 0.5098 |
| gross_profit_factor | 1.0891 |
| gross_win_rate | 0.5230 |
| sharpe_ratio | -2.0074 |
| sortino_ratio | -0.6087 |
| max_drawdown | 0.5370 |
| cagr | -0.2496 |
| net_avg_win | 61.7806 |
| net_avg_loss | -87.2689 |
| avg_hold_time_bars | 14.4245 |
| exposure | 0.2983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

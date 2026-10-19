# EMA Hourly Continuation — AAVE/USDT P12_144

**Symbol:** AAVE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.5369 |
| net_win_rate | 0.4301 |
| gross_profit_factor | 0.7682 |
| gross_win_rate | 0.4323 |
| sharpe_ratio | -4.2495 |
| sortino_ratio | -1.2810 |
| max_drawdown | 0.8023 |
| cagr | -0.4639 |
| net_avg_win | 45.8670 |
| net_avg_loss | -64.4691 |
| avg_hold_time_bars | 31.9613 |
| exposure | 0.6755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

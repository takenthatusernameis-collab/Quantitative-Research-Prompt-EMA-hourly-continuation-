# EMA Hourly Continuation — LUNA/USDT P26_144

**Symbol:** LUNA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.5771 |
| net_win_rate | 0.4461 |
| gross_profit_factor | 0.9281 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -4.9231 |
| sortino_ratio | -1.6937 |
| max_drawdown | 0.8737 |
| cagr | -0.5567 |
| net_avg_win | 44.8272 |
| net_avg_loss | -62.5610 |
| avg_hold_time_bars | 16.2290 |
| exposure | 0.4382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

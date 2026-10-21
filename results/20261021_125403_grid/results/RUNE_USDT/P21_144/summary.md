# EMA Hourly Continuation — RUNE/USDT P21_144

**Symbol:** RUNE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.9447 |
| net_win_rate | 0.5395 |
| gross_profit_factor | 1.1628 |
| gross_win_rate | 0.5395 |
| sharpe_ratio | -0.2511 |
| sortino_ratio | -0.0634 |
| max_drawdown | 0.1275 |
| cagr | -0.0332 |
| net_avg_win | 84.6421 |
| net_avg_loss | -104.9520 |
| avg_hold_time_bars | 45.7368 |
| exposure | 0.6320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

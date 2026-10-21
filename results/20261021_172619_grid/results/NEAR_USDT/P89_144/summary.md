# EMA Hourly Continuation — NEAR/USDT P89_144

**Symbol:** NEAR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.7610 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9690 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.2151 |
| sortino_ratio | -0.2788 |
| max_drawdown | 0.3562 |
| cagr | -0.1205 |
| net_avg_win | 68.5982 |
| net_avg_loss | -90.1365 |
| avg_hold_time_bars | 7.7383 |
| exposure | 0.0900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

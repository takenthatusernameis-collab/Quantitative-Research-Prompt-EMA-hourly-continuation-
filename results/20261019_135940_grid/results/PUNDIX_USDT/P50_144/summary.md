# EMA Hourly Continuation — PUNDIX/USDT P50_144

**Symbol:** PUNDIX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.5772 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9315 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -3.6646 |
| sortino_ratio | -1.1386 |
| max_drawdown | 0.7506 |
| cagr | -0.4209 |
| net_avg_win | 43.3607 |
| net_avg_loss | -70.0518 |
| avg_hold_time_bars | 13.6242 |
| exposure | 0.3016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

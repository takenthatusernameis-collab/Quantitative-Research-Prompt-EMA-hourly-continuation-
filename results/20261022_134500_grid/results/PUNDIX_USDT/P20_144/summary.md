# EMA Hourly Continuation — PUNDIX/USDT P20_144

**Symbol:** PUNDIX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.5610 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.8589 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -3.6425 |
| sortino_ratio | -1.1428 |
| max_drawdown | 0.7588 |
| cagr | -0.4267 |
| net_avg_win | 40.7663 |
| net_avg_loss | -64.2254 |
| avg_hold_time_bars | 25.0596 |
| exposure | 0.5730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

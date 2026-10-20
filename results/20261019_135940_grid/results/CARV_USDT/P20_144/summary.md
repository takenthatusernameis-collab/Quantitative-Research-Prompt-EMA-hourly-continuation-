# EMA Hourly Continuation — CARV/USDT P20_144

**Symbol:** CARV/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.5600 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.8112 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -4.1604 |
| sortino_ratio | -1.3220 |
| max_drawdown | 0.7412 |
| cagr | -0.4671 |
| net_avg_win | 50.1492 |
| net_avg_loss | -71.2503 |
| avg_hold_time_bars | 22.5714 |
| exposure | 0.5246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

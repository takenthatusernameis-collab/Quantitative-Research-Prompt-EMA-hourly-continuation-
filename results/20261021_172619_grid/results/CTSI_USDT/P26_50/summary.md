# EMA Hourly Continuation — CTSI/USDT P26_50

**Symbol:** CTSI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.6173 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8736 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -4.1340 |
| sortino_ratio | -1.3802 |
| max_drawdown | 0.8087 |
| cagr | -0.4701 |
| net_avg_win | 52.4794 |
| net_avg_loss | -68.9660 |
| avg_hold_time_bars | 5.9397 |
| exposure | 0.1477 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

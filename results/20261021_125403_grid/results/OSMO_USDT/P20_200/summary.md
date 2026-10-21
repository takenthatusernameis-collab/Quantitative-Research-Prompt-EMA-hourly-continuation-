# EMA Hourly Continuation — OSMO/USDT P20_200

**Symbol:** OSMO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.9492 |
| net_win_rate | 0.5333 |
| gross_profit_factor | 1.1409 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -0.2664 |
| sortino_ratio | -0.0682 |
| max_drawdown | 0.2488 |
| cagr | -0.0357 |
| net_avg_win | 96.8878 |
| net_avg_loss | -116.6564 |
| avg_hold_time_bars | 44.1460 |
| exposure | 0.6321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

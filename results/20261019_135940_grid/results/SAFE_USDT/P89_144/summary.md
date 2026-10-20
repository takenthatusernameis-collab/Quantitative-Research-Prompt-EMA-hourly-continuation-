# EMA Hourly Continuation — SAFE/USDT P89_144

**Symbol:** SAFE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.4576 |
| net_win_rate | 0.4415 |
| gross_profit_factor | 0.7889 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -4.8534 |
| sortino_ratio | -1.4562 |
| max_drawdown | 0.8402 |
| cagr | -0.5123 |
| net_avg_win | 35.1458 |
| net_avg_loss | -60.7093 |
| avg_hold_time_bars | 6.7815 |
| exposure | 0.1407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

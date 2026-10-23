# EMA Hourly Continuation — BOME/USDT P12_89

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 759 |
| net_profit_factor | 0.5369 |
| net_win_rate | 0.4466 |
| gross_profit_factor | 0.7562 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -4.7576 |
| sortino_ratio | -1.8342 |
| max_drawdown | 0.8974 |
| cagr | -0.5870 |
| net_avg_win | 30.4811 |
| net_avg_loss | -45.8275 |
| avg_hold_time_bars | 14.8195 |
| exposure | 0.5113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

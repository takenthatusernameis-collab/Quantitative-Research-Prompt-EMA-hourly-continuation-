# EMA Hourly Continuation — ETN/USDT P12_200

**Symbol:** ETN/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.5285 |
| net_win_rate | 0.4043 |
| gross_profit_factor | 0.7140 |
| gross_win_rate | 0.4083 |
| sharpe_ratio | -5.4600 |
| sortino_ratio | -1.8832 |
| max_drawdown | 0.8540 |
| cagr | -0.5938 |
| net_avg_win | 46.4398 |
| net_avg_loss | -59.6489 |
| avg_hold_time_bars | 22.0335 |
| exposure | 0.6068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — METIS/USDT P26_144

**Symbol:** METIS/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7254 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.8811 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -1.9819 |
| sortino_ratio | -0.5448 |
| max_drawdown | 0.4761 |
| cagr | -0.2218 |
| net_avg_win | 70.5457 |
| net_avg_loss | -85.5180 |
| avg_hold_time_bars | 27.8021 |
| exposure | 0.4726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

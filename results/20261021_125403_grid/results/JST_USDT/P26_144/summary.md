# EMA Hourly Continuation — JST/USDT P26_144

**Symbol:** JST/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.6810 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0482 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -2.0262 |
| sortino_ratio | -0.5347 |
| max_drawdown | 0.4880 |
| cagr | -0.2206 |
| net_avg_win | 56.9255 |
| net_avg_loss | -86.5593 |
| avg_hold_time_bars | 29.6715 |
| exposure | 0.4619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

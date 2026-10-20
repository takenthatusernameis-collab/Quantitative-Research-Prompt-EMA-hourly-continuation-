# EMA Hourly Continuation — RIO/USDT P55_144

**Symbol:** RIO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.5348 |
| net_win_rate | 0.4211 |
| gross_profit_factor | 0.7244 |
| gross_win_rate | 0.4211 |
| sharpe_ratio | -4.9527 |
| sortino_ratio | -1.6989 |
| max_drawdown | 0.8802 |
| cagr | -0.5594 |
| net_avg_win | 39.8302 |
| net_avg_loss | -54.1872 |
| avg_hold_time_bars | 8.4446 |
| exposure | 0.2311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

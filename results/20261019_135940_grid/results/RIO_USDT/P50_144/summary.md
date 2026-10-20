# EMA Hourly Continuation — RIO/USDT P50_144

**Symbol:** RIO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.5438 |
| net_win_rate | 0.4214 |
| gross_profit_factor | 0.7378 |
| gross_win_rate | 0.4231 |
| sharpe_ratio | -4.9335 |
| sortino_ratio | -1.6931 |
| max_drawdown | 0.8806 |
| cagr | -0.5591 |
| net_avg_win | 41.1377 |
| net_avg_loss | -55.0920 |
| avg_hold_time_bars | 8.7977 |
| exposure | 0.2415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

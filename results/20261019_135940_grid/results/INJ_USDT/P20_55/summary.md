# EMA Hourly Continuation — INJ/USDT P20_55

**Symbol:** INJ/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 952 |
| net_profit_factor | 0.5865 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9473 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -5.4206 |
| sortino_ratio | -2.3560 |
| max_drawdown | 0.9436 |
| cagr | -0.6794 |
| net_avg_win | 29.2516 |
| net_avg_loss | -46.0471 |
| avg_hold_time_bars | 5.2668 |
| exposure | 0.2279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

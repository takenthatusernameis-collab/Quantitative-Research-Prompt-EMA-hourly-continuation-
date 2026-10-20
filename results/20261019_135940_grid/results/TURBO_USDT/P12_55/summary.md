# EMA Hourly Continuation — TURBO/USDT P12_55

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 883 |
| net_profit_factor | 0.6728 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9746 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -5.0702 |
| sortino_ratio | -2.3240 |
| max_drawdown | 0.9051 |
| cagr | -0.6700 |
| net_avg_win | 44.4717 |
| net_avg_loss | -59.1447 |
| avg_hold_time_bars | 7.2299 |
| exposure | 0.3483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

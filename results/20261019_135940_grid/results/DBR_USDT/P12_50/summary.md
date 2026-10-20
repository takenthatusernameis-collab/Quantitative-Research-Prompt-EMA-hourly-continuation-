# EMA Hourly Continuation — DBR/USDT P12_50

**Symbol:** DBR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.5383 |
| net_win_rate | 0.4461 |
| gross_profit_factor | 0.9455 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -6.5768 |
| sortino_ratio | -2.7263 |
| max_drawdown | 0.9358 |
| cagr | -0.7289 |
| net_avg_win | 35.3286 |
| net_avg_loss | -52.8482 |
| avg_hold_time_bars | 9.0364 |
| exposure | 0.3525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

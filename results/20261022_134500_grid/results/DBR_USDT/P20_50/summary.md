# EMA Hourly Continuation — DBR/USDT P20_50

**Symbol:** DBR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.5106 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.9526 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -6.9078 |
| sortino_ratio | -2.7418 |
| max_drawdown | 0.9384 |
| cagr | -0.7403 |
| net_avg_win | 34.6522 |
| net_avg_loss | -53.8688 |
| avg_hold_time_bars | 7.3213 |
| exposure | 0.2644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

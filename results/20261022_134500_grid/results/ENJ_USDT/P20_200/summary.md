# EMA Hourly Continuation — ENJ/USDT P20_200

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.6785 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.9358 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -2.2546 |
| sortino_ratio | -0.6061 |
| max_drawdown | 0.5438 |
| cagr | -0.2527 |
| net_avg_win | 62.0475 |
| net_avg_loss | -85.1942 |
| avg_hold_time_bars | 39.1526 |
| exposure | 0.6502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

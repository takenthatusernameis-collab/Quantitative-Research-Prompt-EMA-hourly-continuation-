# EMA Hourly Continuation — GRT/USDT P20_21

**Symbol:** GRT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 134 |
| net_profit_factor | 0.5850 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.8340 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -2.0365 |
| sortino_ratio | -0.3362 |
| max_drawdown | 0.3599 |
| cagr | -0.1437 |
| net_avg_win | 76.0570 |
| net_avg_loss | -105.4204 |
| avg_hold_time_bars | 4.6269 |
| exposure | 0.0281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

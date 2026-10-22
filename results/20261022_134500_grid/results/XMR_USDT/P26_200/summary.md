# EMA Hourly Continuation — XMR/USDT P26_200

**Symbol:** XMR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.5449 |
| net_win_rate | 0.4594 |
| gross_profit_factor | 0.9257 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -4.9127 |
| sortino_ratio | -1.7084 |
| max_drawdown | 0.8824 |
| cagr | -0.5675 |
| net_avg_win | 37.1516 |
| net_avg_loss | -57.9437 |
| avg_hold_time_bars | 18.7354 |
| exposure | 0.5246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

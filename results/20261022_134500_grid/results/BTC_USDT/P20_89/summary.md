# EMA Hourly Continuation — BTC/USDT P20_89

**Symbol:** BTC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.5028 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 1.1413 |
| gross_win_rate | 0.5287 |
| sharpe_ratio | -5.4183 |
| sortino_ratio | -1.8705 |
| max_drawdown | 0.9348 |
| cagr | -0.6135 |
| net_avg_win | 27.6104 |
| net_avg_loss | -52.7510 |
| avg_hold_time_bars | 14.4699 |
| exposure | 0.4040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — LISTA/USDT P26_50

**Symbol:** LISTA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 834 |
| net_profit_factor | 0.5212 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8414 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -6.3394 |
| sortino_ratio | -2.6866 |
| max_drawdown | 0.9496 |
| cagr | -0.7218 |
| net_avg_win | 27.7086 |
| net_avg_loss | -43.0172 |
| avg_hold_time_bars | 4.6643 |
| exposure | 0.1902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — T/USDT P26_34

**Symbol:** T/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.5495 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9579 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -3.9721 |
| sortino_ratio | -1.1286 |
| max_drawdown | 0.7372 |
| cagr | -0.4048 |
| net_avg_win | 48.1181 |
| net_avg_loss | -78.6408 |
| avg_hold_time_bars | 5.4015 |
| exposure | 0.0956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

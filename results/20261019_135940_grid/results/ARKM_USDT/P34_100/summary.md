# EMA Hourly Continuation — ARKM/USDT P34_100

**Symbol:** ARKM/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 673 |
| net_profit_factor | 0.5831 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.8569 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -4.1074 |
| sortino_ratio | -1.5073 |
| max_drawdown | 0.8331 |
| cagr | -0.5079 |
| net_avg_win | 36.9191 |
| net_avg_loss | -55.7097 |
| avg_hold_time_bars | 8.3863 |
| exposure | 0.2565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — HTX/USDT P21_200

**Symbol:** HTX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.3658 |
| net_win_rate | 0.3636 |
| gross_profit_factor | 0.8569 |
| gross_win_rate | 0.4312 |
| sharpe_ratio | -7.4258 |
| sortino_ratio | -2.1698 |
| max_drawdown | 0.9527 |
| cagr | -0.6987 |
| net_avg_win | 35.1816 |
| net_avg_loss | -54.9573 |
| avg_hold_time_bars | 33.6387 |
| exposure | 0.6530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

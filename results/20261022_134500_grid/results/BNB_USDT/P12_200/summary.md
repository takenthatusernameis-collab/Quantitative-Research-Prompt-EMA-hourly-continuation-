# EMA Hourly Continuation — BNB/USDT P12_200

**Symbol:** BNB/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.4147 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.9419 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -4.9936 |
| sortino_ratio | -1.4349 |
| max_drawdown | 0.8514 |
| cagr | -0.5260 |
| net_avg_win | 31.2492 |
| net_avg_loss | -60.7826 |
| avg_hold_time_bars | 37.1070 |
| exposure | 0.7253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

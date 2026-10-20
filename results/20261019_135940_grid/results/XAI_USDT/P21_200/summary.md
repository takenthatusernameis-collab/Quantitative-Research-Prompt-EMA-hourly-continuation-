# EMA Hourly Continuation — XAI/USDT P21_200

**Symbol:** XAI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7362 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9780 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -1.7540 |
| sortino_ratio | -0.4237 |
| max_drawdown | 0.4488 |
| cagr | -0.1814 |
| net_avg_win | 77.6347 |
| net_avg_loss | -99.8292 |
| avg_hold_time_bars | 55.7911 |
| exposure | 0.7405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

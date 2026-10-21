# EMA Hourly Continuation — UNI/USDT P21_34

**Symbol:** UNI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 231 |
| net_profit_factor | 0.7198 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 0.9962 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -1.4879 |
| sortino_ratio | -0.3251 |
| max_drawdown | 0.3533 |
| cagr | -0.1377 |
| net_avg_win | 68.8025 |
| net_avg_loss | -96.4114 |
| avg_hold_time_bars | 5.0216 |
| exposure | 0.0527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

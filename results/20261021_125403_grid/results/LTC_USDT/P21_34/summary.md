# EMA Hourly Continuation — LTC/USDT P21_34

**Symbol:** LTC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.6186 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9683 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -2.2620 |
| sortino_ratio | -0.4916 |
| max_drawdown | 0.4390 |
| cagr | -0.2000 |
| net_avg_win | 62.1061 |
| net_avg_loss | -96.9412 |
| avg_hold_time_bars | 4.7632 |
| exposure | 0.0494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

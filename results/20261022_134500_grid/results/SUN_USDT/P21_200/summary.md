# EMA Hourly Continuation — SUN/USDT P21_200

**Symbol:** SUN/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.4561 |
| net_win_rate | 0.4182 |
| gross_profit_factor | 0.7807 |
| gross_win_rate | 0.4394 |
| sharpe_ratio | -4.5540 |
| sortino_ratio | -1.1497 |
| max_drawdown | 0.7735 |
| cagr | -0.4422 |
| net_avg_win | 46.8258 |
| net_avg_loss | -73.7950 |
| avg_hold_time_bars | 43.9515 |
| exposure | 0.6563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — DOGE/USDT P26_89

**Symbol:** DOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.4593 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.8243 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -6.3493 |
| sortino_ratio | -2.3487 |
| max_drawdown | 0.9497 |
| cagr | -0.6926 |
| net_avg_win | 25.8215 |
| net_avg_loss | -45.4385 |
| avg_hold_time_bars | 9.6275 |
| exposure | 0.3055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

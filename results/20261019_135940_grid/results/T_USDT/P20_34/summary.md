# EMA Hourly Continuation — T/USDT P20_34

**Symbol:** T/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 900 |
| net_profit_factor | 0.4410 |
| net_win_rate | 0.4300 |
| gross_profit_factor | 0.9853 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -8.8065 |
| sortino_ratio | -3.7293 |
| max_drawdown | 0.9917 |
| cagr | -0.8497 |
| net_avg_win | 20.2176 |
| net_avg_loss | -34.5814 |
| avg_hold_time_bars | 4.4433 |
| exposure | 0.1810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

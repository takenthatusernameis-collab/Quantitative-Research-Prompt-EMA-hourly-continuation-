# EMA Hourly Continuation — TFUEL/USDT P20_100

**Symbol:** TFUEL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 830 |
| net_profit_factor | 0.5493 |
| net_win_rate | 0.4205 |
| gross_profit_factor | 0.8667 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -6.9389 |
| sortino_ratio | -2.7857 |
| max_drawdown | 0.9697 |
| cagr | -0.7459 |
| net_avg_win | 33.8203 |
| net_avg_loss | -44.6729 |
| avg_hold_time_bars | 10.4542 |
| exposure | 0.3926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

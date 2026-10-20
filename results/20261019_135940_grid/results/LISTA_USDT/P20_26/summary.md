# EMA Hourly Continuation — LISTA/USDT P20_26

**Symbol:** LISTA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1018 |
| net_profit_factor | 0.3889 |
| net_win_rate | 0.3851 |
| gross_profit_factor | 0.8724 |
| gross_win_rate | 0.4293 |
| sharpe_ratio | -11.1337 |
| sortino_ratio | -5.2713 |
| max_drawdown | 0.9979 |
| cagr | -0.9274 |
| net_avg_win | 16.1957 |
| net_avg_loss | -26.0812 |
| avg_hold_time_bars | 2.7426 |
| exposure | 0.1365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

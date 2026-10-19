# EMA Hourly Continuation — JASMY/USDT P20_55

**Symbol:** JASMY/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 979 |
| net_profit_factor | 0.5162 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.8669 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -6.2219 |
| sortino_ratio | -2.7369 |
| max_drawdown | 0.9649 |
| cagr | -0.7356 |
| net_avg_win | 22.5236 |
| net_avg_loss | -38.1979 |
| avg_hold_time_bars | 4.7446 |
| exposure | 0.2111 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — HBAR/USDT P12_20

**Symbol:** HBAR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1525 |
| net_profit_factor | 0.2303 |
| net_win_rate | 0.4052 |
| gross_profit_factor | 0.6983 |
| gross_win_rate | 0.4433 |
| sharpe_ratio | -14.7032 |
| sortino_ratio | -8.2331 |
| max_drawdown | 1.0000 |
| cagr | -0.9876 |
| net_avg_win | 4.8408 |
| net_avg_loss | -14.3235 |
| avg_hold_time_bars | 1.9869 |
| exposure | 0.1377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

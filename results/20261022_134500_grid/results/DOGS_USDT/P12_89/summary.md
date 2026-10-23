# EMA Hourly Continuation — DOGS/USDT P12_89

**Symbol:** DOGS/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.6998 |
| net_win_rate | 0.5023 |
| gross_profit_factor | 0.9950 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -3.0210 |
| sortino_ratio | -1.1923 |
| max_drawdown | 0.7111 |
| cagr | -0.4303 |
| net_avg_win | 49.1357 |
| net_avg_loss | -70.8547 |
| avg_hold_time_bars | 14.9125 |
| exposure | 0.5245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

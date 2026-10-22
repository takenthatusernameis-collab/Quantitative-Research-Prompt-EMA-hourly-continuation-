# EMA Hourly Continuation — BIGTIME/USDT P8_100

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.8065 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9592 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -1.5035 |
| sortino_ratio | -0.4601 |
| max_drawdown | 0.4611 |
| cagr | -0.1924 |
| net_avg_win | 76.8444 |
| net_avg_loss | -91.2430 |
| avg_hold_time_bars | 32.3658 |
| exposure | 0.6767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

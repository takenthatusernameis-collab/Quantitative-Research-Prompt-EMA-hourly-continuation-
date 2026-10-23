# EMA Hourly Continuation — ZPAY/USDT P20_21

**Symbol:** ZPAY/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 967 |
| net_profit_factor | 0.2450 |
| net_win_rate | 0.2937 |
| gross_profit_factor | 0.6864 |
| gross_win_rate | 0.3278 |
| sharpe_ratio | -12.7454 |
| sortino_ratio | -5.5977 |
| max_drawdown | 0.9992 |
| cagr | -0.9415 |
| net_avg_win | 11.4153 |
| net_avg_loss | -19.3765 |
| avg_hold_time_bars | 4.9586 |
| exposure | 0.2170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

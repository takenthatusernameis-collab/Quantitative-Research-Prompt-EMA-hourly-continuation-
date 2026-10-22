# EMA Hourly Continuation — ATOM/USDT P21_100

**Symbol:** ATOM/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.5914 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9555 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -3.6917 |
| sortino_ratio | -1.3072 |
| max_drawdown | 0.8074 |
| cagr | -0.4669 |
| net_avg_win | 36.7085 |
| net_avg_loss | -60.7168 |
| avg_hold_time_bars | 14.2812 |
| exposure | 0.4109 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

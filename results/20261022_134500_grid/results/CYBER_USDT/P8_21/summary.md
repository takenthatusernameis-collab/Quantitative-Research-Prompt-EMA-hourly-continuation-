# EMA Hourly Continuation — CYBER/USDT P8_21

**Symbol:** CYBER/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1595 |
| net_profit_factor | 0.4287 |
| net_win_rate | 0.4351 |
| gross_profit_factor | 0.8444 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -10.9772 |
| sortino_ratio | -6.1945 |
| max_drawdown | 0.9996 |
| cagr | -0.9546 |
| net_avg_win | 10.8090 |
| net_avg_loss | -19.4197 |
| avg_hold_time_bars | 3.4991 |
| exposure | 0.2537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

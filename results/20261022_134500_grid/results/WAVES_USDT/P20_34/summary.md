# EMA Hourly Continuation — WAVES/USDT P20_34

**Symbol:** WAVES/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1284 |
| net_profit_factor | 0.3154 |
| net_win_rate | 0.3559 |
| gross_profit_factor | 0.8492 |
| gross_win_rate | 0.4058 |
| sharpe_ratio | -14.5906 |
| sortino_ratio | -7.5527 |
| max_drawdown | 1.0000 |
| cagr | -0.9818 |
| net_avg_win | 10.0813 |
| net_avg_loss | -17.6623 |
| avg_hold_time_bars | 2.8045 |
| exposure | 0.1637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

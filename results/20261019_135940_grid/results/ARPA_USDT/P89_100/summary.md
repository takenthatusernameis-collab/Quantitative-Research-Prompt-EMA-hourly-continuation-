# EMA Hourly Continuation — ARPA/USDT P89_100

**Symbol:** ARPA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.2241 |
| net_win_rate | 0.3543 |
| gross_profit_factor | 0.6507 |
| gross_win_rate | 0.4126 |
| sharpe_ratio | -10.4577 |
| sortino_ratio | -3.8650 |
| max_drawdown | 0.9942 |
| cagr | -0.8706 |
| net_avg_win | 12.4323 |
| net_avg_loss | -30.4378 |
| avg_hold_time_bars | 2.8512 |
| exposure | 0.0841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

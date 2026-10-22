# EMA Hourly Continuation — FLOKI/USDT P34_50

**Symbol:** FLOKI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 983 |
| net_profit_factor | 0.4175 |
| net_win_rate | 0.4191 |
| gross_profit_factor | 0.7720 |
| gross_win_rate | 0.4374 |
| sharpe_ratio | -9.6497 |
| sortino_ratio | -4.2902 |
| max_drawdown | 0.9959 |
| cagr | -0.8865 |
| net_avg_win | 17.3238 |
| net_avg_loss | -29.9389 |
| avg_hold_time_bars | 2.4883 |
| exposure | 0.1112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

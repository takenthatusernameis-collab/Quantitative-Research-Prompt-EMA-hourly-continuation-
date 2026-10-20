# EMA Hourly Continuation — ENJ/USDT P21_55

**Symbol:** ENJ/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 958 |
| net_profit_factor | 0.4921 |
| net_win_rate | 0.4415 |
| gross_profit_factor | 0.8968 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -7.4261 |
| sortino_ratio | -3.2522 |
| max_drawdown | 0.9820 |
| cagr | -0.7946 |
| net_avg_win | 22.4727 |
| net_avg_loss | -36.1087 |
| avg_hold_time_bars | 5.1044 |
| exposure | 0.2223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

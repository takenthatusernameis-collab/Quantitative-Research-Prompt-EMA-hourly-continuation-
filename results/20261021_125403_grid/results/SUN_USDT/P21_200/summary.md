# EMA Hourly Continuation — SUN/USDT P21_200

**Symbol:** SUN/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.5886 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.8328 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -2.8131 |
| sortino_ratio | -0.6498 |
| max_drawdown | 0.5603 |
| cagr | -0.2648 |
| net_avg_win | 63.8230 |
| net_avg_loss | -88.6439 |
| avg_hold_time_bars | 53.5353 |
| exposure | 0.6517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

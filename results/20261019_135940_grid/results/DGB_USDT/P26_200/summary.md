# EMA Hourly Continuation — DGB/USDT P26_200

**Symbol:** DGB/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6653 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.9127 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -3.3529 |
| sortino_ratio | -1.0346 |
| max_drawdown | 0.7507 |
| cagr | -0.3905 |
| net_avg_win | 63.4405 |
| net_avg_loss | -81.4679 |
| avg_hold_time_bars | 25.3388 |
| exposure | 0.5575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

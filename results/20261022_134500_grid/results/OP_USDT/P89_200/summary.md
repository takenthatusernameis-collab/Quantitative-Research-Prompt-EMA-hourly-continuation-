# EMA Hourly Continuation — OP/USDT P89_200

**Symbol:** OP/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.6886 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 1.0562 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -2.5382 |
| sortino_ratio | -0.7362 |
| max_drawdown | 0.6149 |
| cagr | -0.2924 |
| net_avg_win | 62.0125 |
| net_avg_loss | -89.6180 |
| avg_hold_time_bars | 9.9783 |
| exposure | 0.1882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

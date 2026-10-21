# EMA Hourly Continuation — ZEC/USDT P8_21

**Symbol:** ZEC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6052 |
| net_win_rate | 0.4549 |
| gross_profit_factor | 0.7886 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -2.9328 |
| sortino_ratio | -0.9004 |
| max_drawdown | 0.6458 |
| cagr | -0.3385 |
| net_avg_win | 46.7001 |
| net_avg_loss | -64.4014 |
| avg_hold_time_bars | 5.8777 |
| exposure | 0.1245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

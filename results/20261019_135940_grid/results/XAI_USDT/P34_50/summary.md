# EMA Hourly Continuation — XAI/USDT P34_50

**Symbol:** XAI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 984 |
| net_profit_factor | 0.4767 |
| net_win_rate | 0.4207 |
| gross_profit_factor | 0.8688 |
| gross_win_rate | 0.4533 |
| sharpe_ratio | -8.7616 |
| sortino_ratio | -3.8985 |
| max_drawdown | 0.9923 |
| cagr | -0.8526 |
| net_avg_win | 21.8212 |
| net_avg_loss | -33.2498 |
| avg_hold_time_bars | 2.9624 |
| exposure | 0.1325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

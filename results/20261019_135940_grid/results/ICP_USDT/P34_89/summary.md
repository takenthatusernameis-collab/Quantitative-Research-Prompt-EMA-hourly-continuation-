# EMA Hourly Continuation — ICP/USDT P34_89

**Symbol:** ICP/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.5301 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.8833 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -5.2341 |
| sortino_ratio | -1.9654 |
| max_drawdown | 0.9093 |
| cagr | -0.6121 |
| net_avg_win | 30.9244 |
| net_avg_loss | -50.6789 |
| avg_hold_time_bars | 7.1419 |
| exposure | 0.2311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

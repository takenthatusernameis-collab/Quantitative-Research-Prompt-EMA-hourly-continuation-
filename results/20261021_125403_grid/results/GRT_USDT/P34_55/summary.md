# EMA Hourly Continuation — GRT/USDT P34_55

**Symbol:** GRT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.7786 |
| net_win_rate | 0.5253 |
| gross_profit_factor | 1.0942 |
| gross_win_rate | 0.5253 |
| sharpe_ratio | -1.3529 |
| sortino_ratio | -0.3465 |
| max_drawdown | 0.3610 |
| cagr | -0.1465 |
| net_avg_win | 69.7992 |
| net_avg_loss | -99.2089 |
| avg_hold_time_bars | 5.5253 |
| exposure | 0.0790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

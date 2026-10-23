# EMA Hourly Continuation — MERL/USDT P34_100

**Symbol:** MERL/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.6737 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9254 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -2.9192 |
| sortino_ratio | -1.0138 |
| max_drawdown | 0.7121 |
| cagr | -0.3789 |
| net_avg_win | 49.0949 |
| net_avg_loss | -68.8735 |
| avg_hold_time_bars | 10.2471 |
| exposure | 0.2816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

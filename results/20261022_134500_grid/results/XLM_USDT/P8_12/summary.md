# EMA Hourly Continuation — XLM/USDT P8_12

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1926 |
| net_profit_factor | 0.0664 |
| net_win_rate | 0.3229 |
| gross_profit_factor | 0.5367 |
| gross_win_rate | 0.4019 |
| sharpe_ratio | -21.3725 |
| sortino_ratio | -13.9624 |
| max_drawdown | 1.0000 |
| cagr | -0.9995 |
| net_avg_win | 1.1441 |
| net_avg_loss | -8.2144 |
| avg_hold_time_bars | 1.7233 |
| exposure | 0.1509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

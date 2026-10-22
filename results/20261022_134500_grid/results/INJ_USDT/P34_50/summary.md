# EMA Hourly Continuation — INJ/USDT P34_50

**Symbol:** INJ/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 893 |
| net_profit_factor | 0.3932 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.7523 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -8.3773 |
| sortino_ratio | -3.5339 |
| max_drawdown | 0.9891 |
| cagr | -0.8335 |
| net_avg_win | 16.5596 |
| net_avg_loss | -32.2090 |
| avg_hold_time_bars | 2.5778 |
| exposure | 0.1046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

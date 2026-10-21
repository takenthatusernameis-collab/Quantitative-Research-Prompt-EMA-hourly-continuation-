# EMA Hourly Continuation — METIS/USDT P8_89

**Symbol:** METIS/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.8201 |
| net_win_rate | 0.4960 |
| gross_profit_factor | 0.9838 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -1.4232 |
| sortino_ratio | -0.4520 |
| max_drawdown | 0.4391 |
| cagr | -0.1893 |
| net_avg_win | 76.2351 |
| net_avg_loss | -91.4606 |
| avg_hold_time_bars | 28.3644 |
| exposure | 0.6369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

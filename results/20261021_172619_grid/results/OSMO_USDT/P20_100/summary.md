# EMA Hourly Continuation — OSMO/USDT P20_100

**Symbol:** OSMO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.8755 |
| net_win_rate | 0.5255 |
| gross_profit_factor | 1.1164 |
| gross_win_rate | 0.5255 |
| sharpe_ratio | -0.9640 |
| sortino_ratio | -0.3010 |
| max_drawdown | 0.4239 |
| cagr | -0.1323 |
| net_avg_win | 85.3786 |
| net_avg_loss | -108.0105 |
| avg_hold_time_bars | 20.4489 |
| exposure | 0.4369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

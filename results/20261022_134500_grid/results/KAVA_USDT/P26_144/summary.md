# EMA Hourly Continuation — KAVA/USDT P26_144

**Symbol:** KAVA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.5759 |
| net_win_rate | 0.4552 |
| gross_profit_factor | 0.9279 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -4.4977 |
| sortino_ratio | -1.4620 |
| max_drawdown | 0.8438 |
| cagr | -0.5089 |
| net_avg_win | 46.3208 |
| net_avg_loss | -67.2104 |
| avg_hold_time_bars | 19.7612 |
| exposure | 0.4815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — 1INCH/USDT P8_34

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 746 |
| net_profit_factor | 0.6844 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9418 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -3.1699 |
| sortino_ratio | -1.2406 |
| max_drawdown | 0.7624 |
| cagr | -0.4334 |
| net_avg_win | 44.9096 |
| net_avg_loss | -63.5379 |
| avg_hold_time_bars | 8.5429 |
| exposure | 0.2897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — MAGIC/USDT P20_89

**Symbol:** MAGIC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.8109 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 1.0308 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -1.6758 |
| sortino_ratio | -0.5520 |
| max_drawdown | 0.5204 |
| cagr | -0.2253 |
| net_avg_win | 76.0063 |
| net_avg_loss | -95.5197 |
| avg_hold_time_bars | 18.1682 |
| exposure | 0.4369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

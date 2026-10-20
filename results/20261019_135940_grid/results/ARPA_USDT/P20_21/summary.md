# EMA Hourly Continuation — ARPA/USDT P20_21

**Symbol:** ARPA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1295 |
| net_profit_factor | 0.1471 |
| net_win_rate | 0.2981 |
| gross_profit_factor | 0.6476 |
| gross_win_rate | 0.3830 |
| sharpe_ratio | -18.0009 |
| sortino_ratio | -9.7342 |
| max_drawdown | 1.0000 |
| cagr | -0.9953 |
| net_avg_win | 4.4691 |
| net_avg_loss | -12.8988 |
| avg_hold_time_bars | 2.2286 |
| exposure | 0.1306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

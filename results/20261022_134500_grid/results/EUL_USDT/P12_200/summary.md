# EMA Hourly Continuation — EUL/USDT P12_200

**Symbol:** EUL/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6088 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8593 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -3.1224 |
| sortino_ratio | -0.8792 |
| max_drawdown | 0.6743 |
| cagr | -0.3492 |
| net_avg_win | 54.3332 |
| net_avg_loss | -75.6419 |
| avg_hold_time_bars | 37.5947 |
| exposure | 0.7040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

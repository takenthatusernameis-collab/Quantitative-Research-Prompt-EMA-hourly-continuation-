# EMA Hourly Continuation — TRADE/USDT P100_200

**Symbol:** TRADE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.3966 |
| net_win_rate | 0.3571 |
| gross_profit_factor | 0.5879 |
| gross_win_rate | 0.3604 |
| sharpe_ratio | -5.0941 |
| sortino_ratio | -1.2512 |
| max_drawdown | 0.7941 |
| cagr | -0.4579 |
| net_avg_win | 46.9065 |
| net_avg_loss | -65.7104 |
| avg_hold_time_bars | 10.8247 |
| exposure | 0.1515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CARV/USDT P26_50

**Symbol:** CARV/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.4454 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.8481 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -6.4862 |
| sortino_ratio | -2.6111 |
| max_drawdown | 0.9260 |
| cagr | -0.7206 |
| net_avg_win | 24.7534 |
| net_avg_loss | -46.0581 |
| avg_hold_time_bars | 5.0982 |
| exposure | 0.1899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

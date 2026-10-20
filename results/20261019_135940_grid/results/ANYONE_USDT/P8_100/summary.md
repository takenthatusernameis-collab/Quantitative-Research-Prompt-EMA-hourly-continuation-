# EMA Hourly Continuation — ANYONE/USDT P8_100

**Symbol:** ANYONE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.7234 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.9148 |
| gross_win_rate | 0.4761 |
| sharpe_ratio | -2.9721 |
| sortino_ratio | -1.1110 |
| max_drawdown | 0.7280 |
| cagr | -0.4047 |
| net_avg_win | 61.8237 |
| net_avg_loss | -74.2697 |
| avg_hold_time_bars | 20.2755 |
| exposure | 0.6434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

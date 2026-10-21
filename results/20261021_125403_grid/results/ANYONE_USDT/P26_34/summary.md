# EMA Hourly Continuation — ANYONE/USDT P26_34

**Symbol:** ANYONE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.5982 |
| net_win_rate | 0.4405 |
| gross_profit_factor | 0.7706 |
| gross_win_rate | 0.4405 |
| sharpe_ratio | -2.5071 |
| sortino_ratio | -0.5643 |
| max_drawdown | 0.4891 |
| cagr | -0.2289 |
| net_avg_win | 66.1277 |
| net_avg_loss | -87.0420 |
| avg_hold_time_bars | 5.9559 |
| exposure | 0.0683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

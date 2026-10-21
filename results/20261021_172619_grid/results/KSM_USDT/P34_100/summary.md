# EMA Hourly Continuation — KSM/USDT P34_100

**Symbol:** KSM/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.8090 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.0633 |
| gross_win_rate | 0.5173 |
| sharpe_ratio | -1.3862 |
| sortino_ratio | -0.4147 |
| max_drawdown | 0.4563 |
| cagr | -0.1741 |
| net_avg_win | 72.0983 |
| net_avg_loss | -95.5204 |
| avg_hold_time_bars | 13.6374 |
| exposure | 0.2684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — WIN/USDT P89_100

**Symbol:** WIN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 572 |
| net_profit_factor | 0.0951 |
| net_win_rate | 0.3024 |
| gross_profit_factor | 0.4292 |
| gross_win_rate | 0.3671 |
| sharpe_ratio | -11.9471 |
| sortino_ratio | -4.3545 |
| max_drawdown | 0.9977 |
| cagr | -0.9105 |
| net_avg_win | 6.0634 |
| net_avg_loss | -27.6332 |
| avg_hold_time_bars | 2.3304 |
| exposure | 0.0606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

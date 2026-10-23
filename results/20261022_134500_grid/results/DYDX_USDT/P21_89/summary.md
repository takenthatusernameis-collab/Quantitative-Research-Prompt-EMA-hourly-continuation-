# EMA Hourly Continuation — DYDX/USDT P21_89

**Symbol:** DYDX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.6522 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9757 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -3.7950 |
| sortino_ratio | -1.4120 |
| max_drawdown | 0.8202 |
| cagr | -0.4869 |
| net_avg_win | 45.6390 |
| net_avg_loss | -64.5617 |
| avg_hold_time_bars | 12.6825 |
| exposure | 0.4012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

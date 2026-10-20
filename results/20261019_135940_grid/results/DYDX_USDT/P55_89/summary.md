# EMA Hourly Continuation — DYDX/USDT P55_89

**Symbol:** DYDX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.5419 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9881 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -5.2835 |
| sortino_ratio | -1.9364 |
| max_drawdown | 0.9110 |
| cagr | -0.6157 |
| net_avg_win | 32.9996 |
| net_avg_loss | -55.4536 |
| avg_hold_time_bars | 3.7749 |
| exposure | 0.1174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

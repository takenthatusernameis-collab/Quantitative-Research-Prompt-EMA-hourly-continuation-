# EMA Hourly Continuation — JUP/USDT P20_21

**Symbol:** JUP/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 112 |
| net_profit_factor | 0.7597 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0062 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.9332 |
| sortino_ratio | -0.1417 |
| max_drawdown | 0.2247 |
| cagr | -0.0631 |
| net_avg_win | 85.2108 |
| net_avg_loss | -112.1623 |
| avg_hold_time_bars | 4.4554 |
| exposure | 0.0227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

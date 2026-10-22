# EMA Hourly Continuation — RIO/USDT P21_50

**Symbol:** RIO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.7577 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.8910 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -1.8641 |
| sortino_ratio | -0.5445 |
| max_drawdown | 0.4864 |
| cagr | -0.2227 |
| net_avg_win | 74.2667 |
| net_avg_loss | -86.5337 |
| avg_hold_time_bars | 8.3134 |
| exposure | 0.1595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

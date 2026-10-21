# EMA Hourly Continuation — SUI/USDT P20_100

**Symbol:** SUI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.8687 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.0594 |
| gross_win_rate | 0.5173 |
| sharpe_ratio | -0.8795 |
| sortino_ratio | -0.2632 |
| max_drawdown | 0.3853 |
| cagr | -0.1170 |
| net_avg_win | 79.3138 |
| net_avg_loss | -97.8516 |
| avg_hold_time_bars | 19.2425 |
| exposure | 0.3787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

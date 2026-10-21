# EMA Hourly Continuation — REQ/USDT P21_34

**Symbol:** REQ/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.5052 |
| net_win_rate | 0.4403 |
| gross_profit_factor | 0.8661 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -5.2785 |
| sortino_ratio | -1.6149 |
| max_drawdown | 0.8517 |
| cagr | -0.5290 |
| net_avg_win | 43.5635 |
| net_avg_loss | -67.8237 |
| avg_hold_time_bars | 5.6637 |
| exposure | 0.1164 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ACE/USDT P8_34

**Symbol:** ACE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 999 |
| net_profit_factor | 0.5134 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.9052 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -5.4480 |
| sortino_ratio | -2.4300 |
| max_drawdown | 0.9441 |
| cagr | -0.6814 |
| net_avg_win | 21.2400 |
| net_avg_loss | -36.6093 |
| avg_hold_time_bars | 8.2362 |
| exposure | 0.3723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

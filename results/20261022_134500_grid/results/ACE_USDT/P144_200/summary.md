# EMA Hourly Continuation — ACE/USDT P144_200

**Symbol:** ACE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.5833 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.9345 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -3.3940 |
| sortino_ratio | -0.8826 |
| max_drawdown | 0.6863 |
| cagr | -0.3461 |
| net_avg_win | 58.2587 |
| net_avg_loss | -85.7647 |
| avg_hold_time_bars | 6.5409 |
| exposure | 0.1012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

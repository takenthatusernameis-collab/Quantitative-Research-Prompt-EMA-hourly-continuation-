# EMA Hourly Continuation — ACE/USDT P34_89

**Symbol:** ACE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.8176 |
| net_win_rate | 0.5146 |
| gross_profit_factor | 1.0676 |
| gross_win_rate | 0.5146 |
| sharpe_ratio | -1.2996 |
| sortino_ratio | -0.3779 |
| max_drawdown | 0.4103 |
| cagr | -0.1606 |
| net_avg_win | 75.4582 |
| net_avg_loss | -97.8327 |
| avg_hold_time_bars | 13.0971 |
| exposure | 0.2442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

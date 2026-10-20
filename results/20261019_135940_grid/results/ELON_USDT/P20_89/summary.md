# EMA Hourly Continuation — ELON/USDT P20_89

**Symbol:** ELON/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 784 |
| net_profit_factor | 0.4754 |
| net_win_rate | 0.4247 |
| gross_profit_factor | 0.7625 |
| gross_win_rate | 0.4298 |
| sharpe_ratio | -6.5526 |
| sortino_ratio | -2.5799 |
| max_drawdown | 0.9587 |
| cagr | -0.7153 |
| net_avg_win | 26.0538 |
| net_avg_loss | -40.4647 |
| avg_hold_time_bars | 9.5587 |
| exposure | 0.3406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

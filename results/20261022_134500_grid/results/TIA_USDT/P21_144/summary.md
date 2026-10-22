# EMA Hourly Continuation — TIA/USDT P21_144

**Symbol:** TIA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.7838 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 1.0276 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -1.7044 |
| sortino_ratio | -0.5005 |
| max_drawdown | 0.4540 |
| cagr | -0.2086 |
| net_avg_win | 75.9867 |
| net_avg_loss | -96.4914 |
| avg_hold_time_bars | 29.5671 |
| exposure | 0.5712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

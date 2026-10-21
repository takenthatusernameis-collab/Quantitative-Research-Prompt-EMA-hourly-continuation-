# EMA Hourly Continuation — KSM/USDT P8_50

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.6847 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.8884 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -3.1175 |
| sortino_ratio | -1.1912 |
| max_drawdown | 0.7503 |
| cagr | -0.4217 |
| net_avg_win | 47.5964 |
| net_avg_loss | -62.7061 |
| avg_hold_time_bars | 13.8136 |
| exposure | 0.4515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

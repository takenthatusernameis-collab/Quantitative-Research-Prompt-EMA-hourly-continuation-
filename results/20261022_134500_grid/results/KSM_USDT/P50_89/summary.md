# EMA Hourly Continuation — KSM/USDT P50_89

**Symbol:** KSM/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.4396 |
| net_win_rate | 0.4409 |
| gross_profit_factor | 0.8119 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -6.4843 |
| sortino_ratio | -2.3284 |
| max_drawdown | 0.9473 |
| cagr | -0.6873 |
| net_avg_win | 25.8567 |
| net_avg_loss | -46.3766 |
| avg_hold_time_bars | 4.9232 |
| exposure | 0.1457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

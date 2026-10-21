# EMA Hourly Continuation — KSM/USDT P20_50

**Symbol:** KSM/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.6568 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9111 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -3.1893 |
| sortino_ratio | -1.0604 |
| max_drawdown | 0.7130 |
| cagr | -0.3848 |
| net_avg_win | 52.4877 |
| net_avg_loss | -72.3147 |
| avg_hold_time_bars | 7.7652 |
| exposure | 0.1910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

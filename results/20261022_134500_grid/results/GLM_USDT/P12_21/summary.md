# EMA Hourly Continuation — GLM/USDT P12_21

**Symbol:** GLM/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1379 |
| net_profit_factor | 0.3257 |
| net_win_rate | 0.4213 |
| gross_profit_factor | 0.8379 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -12.0656 |
| sortino_ratio | -6.3959 |
| max_drawdown | 0.9997 |
| cagr | -0.9603 |
| net_avg_win | 8.3120 |
| net_avg_loss | -18.5793 |
| avg_hold_time_bars | 3.0109 |
| exposure | 0.1887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

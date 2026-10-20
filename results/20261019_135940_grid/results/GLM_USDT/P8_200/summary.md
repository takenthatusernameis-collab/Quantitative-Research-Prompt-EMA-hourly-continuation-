# EMA Hourly Continuation — GLM/USDT P8_200

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.6079 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8878 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -3.4984 |
| sortino_ratio | -1.0309 |
| max_drawdown | 0.7355 |
| cagr | -0.3891 |
| net_avg_win | 54.4985 |
| net_avg_loss | -75.1369 |
| avg_hold_time_bars | 37.8533 |
| exposure | 0.7622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

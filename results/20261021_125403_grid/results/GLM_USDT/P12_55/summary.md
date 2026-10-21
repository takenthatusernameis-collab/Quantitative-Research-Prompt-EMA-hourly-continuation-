# EMA Hourly Continuation — GLM/USDT P12_55

**Symbol:** GLM/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.7054 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -2.9743 |
| sortino_ratio | -1.1116 |
| max_drawdown | 0.7398 |
| cagr | -0.3990 |
| net_avg_win | 51.7339 |
| net_avg_loss | -70.3869 |
| avg_hold_time_bars | 12.4824 |
| exposure | 0.3870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

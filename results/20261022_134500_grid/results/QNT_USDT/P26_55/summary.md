# EMA Hourly Continuation — QNT/USDT P26_55

**Symbol:** QNT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1039 |
| net_profit_factor | 0.3678 |
| net_win_rate | 0.4418 |
| gross_profit_factor | 0.8278 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -8.8270 |
| sortino_ratio | -4.0332 |
| max_drawdown | 0.9937 |
| cagr | -0.8651 |
| net_avg_win | 12.5939 |
| net_avg_loss | -27.0953 |
| avg_hold_time_bars | 3.5852 |
| exposure | 0.1693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — UQC/USDT P34_89

**Symbol:** UQC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.1965 |
| net_win_rate | 0.2428 |
| gross_profit_factor | 0.4115 |
| gross_win_rate | 0.2768 |
| sharpe_ratio | -9.4626 |
| sortino_ratio | -2.6792 |
| max_drawdown | 0.9771 |
| cagr | -0.7763 |
| net_avg_win | 25.6996 |
| net_avg_loss | -41.9345 |
| avg_hold_time_bars | 23.6188 |
| exposure | 0.4094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

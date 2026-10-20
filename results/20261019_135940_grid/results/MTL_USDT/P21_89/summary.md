# EMA Hourly Continuation — MTL/USDT P21_89

**Symbol:** MTL/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.5116 |
| net_win_rate | 0.4353 |
| gross_profit_factor | 0.8638 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -5.2484 |
| sortino_ratio | -1.7871 |
| max_drawdown | 0.8937 |
| cagr | -0.5834 |
| net_avg_win | 36.0062 |
| net_avg_loss | -54.2478 |
| avg_hold_time_bars | 17.2891 |
| exposure | 0.4655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

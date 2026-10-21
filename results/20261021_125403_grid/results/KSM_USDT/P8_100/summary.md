# EMA Hourly Continuation — KSM/USDT P8_100

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.7092 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.8756 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -2.5673 |
| sortino_ratio | -0.7871 |
| max_drawdown | 0.6062 |
| cagr | -0.3038 |
| net_avg_win | 67.7458 |
| net_avg_loss | -81.4995 |
| avg_hold_time_bars | 31.7966 |
| exposure | 0.6750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

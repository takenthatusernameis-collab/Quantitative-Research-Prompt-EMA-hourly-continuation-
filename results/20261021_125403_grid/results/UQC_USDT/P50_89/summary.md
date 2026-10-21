# EMA Hourly Continuation — UQC/USDT P50_89

**Symbol:** UQC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.2015 |
| net_win_rate | 0.2097 |
| gross_profit_factor | 0.3320 |
| gross_win_rate | 0.2339 |
| sharpe_ratio | -7.8088 |
| sortino_ratio | -1.7673 |
| max_drawdown | 0.9117 |
| cagr | -0.6180 |
| net_avg_win | 44.2520 |
| net_avg_loss | -58.2567 |
| avg_hold_time_bars | 28.3669 |
| exposure | 0.3184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

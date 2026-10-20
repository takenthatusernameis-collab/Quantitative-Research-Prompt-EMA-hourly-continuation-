# EMA Hourly Continuation — UQC/USDT P34_55

**Symbol:** UQC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.1121 |
| net_win_rate | 0.2417 |
| gross_profit_factor | 0.2942 |
| gross_win_rate | 0.2595 |
| sharpe_ratio | -9.6292 |
| sortino_ratio | -2.7595 |
| max_drawdown | 0.9777 |
| cagr | -0.7784 |
| net_avg_win | 12.9919 |
| net_avg_loss | -36.9487 |
| avg_hold_time_bars | 26.5954 |
| exposure | 0.4730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

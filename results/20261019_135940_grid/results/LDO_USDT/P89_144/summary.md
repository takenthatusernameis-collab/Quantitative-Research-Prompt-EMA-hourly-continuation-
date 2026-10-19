# EMA Hourly Continuation — LDO/USDT P89_144

**Symbol:** LDO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.4661 |
| net_win_rate | 0.4371 |
| gross_profit_factor | 0.7654 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -4.9976 |
| sortino_ratio | -1.5782 |
| max_drawdown | 0.8640 |
| cagr | -0.5330 |
| net_avg_win | 33.9697 |
| net_avg_loss | -56.6007 |
| avg_hold_time_bars | 5.0898 |
| exposure | 0.1159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

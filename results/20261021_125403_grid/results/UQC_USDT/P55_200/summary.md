# EMA Hourly Continuation — UQC/USDT P55_200

**Symbol:** UQC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 172 |
| net_profit_factor | 0.3465 |
| net_win_rate | 0.3023 |
| gross_profit_factor | 0.4510 |
| gross_win_rate | 0.3023 |
| sharpe_ratio | -4.2888 |
| sortino_ratio | -0.7834 |
| max_drawdown | 0.6154 |
| cagr | -0.3153 |
| net_avg_win | 62.7343 |
| net_avg_loss | -78.4641 |
| avg_hold_time_bars | 71.9535 |
| exposure | 0.5601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

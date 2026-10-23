# EMA Hourly Continuation — CFG/USDT P21_26

**Symbol:** CFG/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 959 |
| net_profit_factor | 0.1617 |
| net_win_rate | 0.3358 |
| gross_profit_factor | 0.4794 |
| gross_win_rate | 0.3670 |
| sharpe_ratio | -12.8240 |
| sortino_ratio | -5.7531 |
| max_drawdown | 0.9995 |
| cagr | -0.9510 |
| net_avg_win | 5.9889 |
| net_avg_loss | -18.7179 |
| avg_hold_time_bars | 6.7456 |
| exposure | 0.2940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

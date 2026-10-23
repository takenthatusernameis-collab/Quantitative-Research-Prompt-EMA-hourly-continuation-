# EMA Hourly Continuation — CKB/USDT P100_144

**Symbol:** CKB/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.4900 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8672 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -4.8975 |
| sortino_ratio | -1.5756 |
| max_drawdown | 0.8597 |
| cagr | -0.5371 |
| net_avg_win | 33.8240 |
| net_avg_loss | -60.9965 |
| avg_hold_time_bars | 4.2587 |
| exposure | 0.1003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

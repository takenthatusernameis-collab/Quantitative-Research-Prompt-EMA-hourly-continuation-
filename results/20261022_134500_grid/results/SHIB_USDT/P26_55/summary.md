# EMA Hourly Continuation — SHIB/USDT P26_55

**Symbol:** SHIB/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 921 |
| net_profit_factor | 0.4562 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.9137 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -8.1623 |
| sortino_ratio | -3.5224 |
| max_drawdown | 0.9881 |
| cagr | -0.8240 |
| net_avg_win | 20.2978 |
| net_avg_loss | -35.3879 |
| avg_hold_time_bars | 3.9294 |
| exposure | 0.1645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

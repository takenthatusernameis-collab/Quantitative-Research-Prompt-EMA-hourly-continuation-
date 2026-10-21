# EMA Hourly Continuation — IOTA/USDT P34_89

**Symbol:** IOTA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.6887 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.9030 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -2.7323 |
| sortino_ratio | -0.8325 |
| max_drawdown | 0.6490 |
| cagr | -0.3171 |
| net_avg_win | 64.0108 |
| net_avg_loss | -81.1359 |
| avg_hold_time_bars | 10.0350 |
| exposure | 0.2085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

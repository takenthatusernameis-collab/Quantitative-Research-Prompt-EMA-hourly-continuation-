# EMA Hourly Continuation — DBR/USDT P26_89

**Symbol:** DBR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.4661 |
| net_win_rate | 0.4354 |
| gross_profit_factor | 0.8198 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -5.9947 |
| sortino_ratio | -2.1117 |
| max_drawdown | 0.8757 |
| cagr | -0.6450 |
| net_avg_win | 34.8767 |
| net_avg_loss | -57.7003 |
| avg_hold_time_bars | 10.9105 |
| exposure | 0.3121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

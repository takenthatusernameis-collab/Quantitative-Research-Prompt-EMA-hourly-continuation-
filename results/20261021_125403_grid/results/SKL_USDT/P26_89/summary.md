# EMA Hourly Continuation — SKL/USDT P26_89

**Symbol:** SKL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.7221 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9001 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -2.2127 |
| sortino_ratio | -0.6756 |
| max_drawdown | 0.5776 |
| cagr | -0.2669 |
| net_avg_win | 64.5307 |
| net_avg_loss | -80.8374 |
| avg_hold_time_bars | 16.0523 |
| exposure | 0.3349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

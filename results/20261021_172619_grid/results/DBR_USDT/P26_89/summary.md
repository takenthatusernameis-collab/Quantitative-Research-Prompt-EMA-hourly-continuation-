# EMA Hourly Continuation — DBR/USDT P26_89

**Symbol:** DBR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.6667 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9167 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -2.6142 |
| sortino_ratio | -0.7701 |
| max_drawdown | 0.5101 |
| cagr | -0.2956 |
| net_avg_win | 61.9827 |
| net_avg_loss | -85.6152 |
| avg_hold_time_bars | 15.0559 |
| exposure | 0.2911 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

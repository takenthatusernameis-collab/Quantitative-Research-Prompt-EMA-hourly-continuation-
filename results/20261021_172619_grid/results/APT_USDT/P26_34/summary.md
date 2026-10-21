# EMA Hourly Continuation — APT/USDT P26_34

**Symbol:** APT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 157 |
| net_profit_factor | 0.6919 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9566 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -1.4150 |
| sortino_ratio | -0.2543 |
| max_drawdown | 0.3247 |
| cagr | -0.1096 |
| net_avg_win | 73.7855 |
| net_avg_loss | -102.6367 |
| avg_hold_time_bars | 5.5287 |
| exposure | 0.0395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

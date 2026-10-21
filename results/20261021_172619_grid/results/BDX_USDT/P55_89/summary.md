# EMA Hourly Continuation — BDX/USDT P55_89

**Symbol:** BDX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 213 |
| net_profit_factor | 0.3802 |
| net_win_rate | 0.3991 |
| gross_profit_factor | 0.6364 |
| gross_win_rate | 0.3991 |
| sharpe_ratio | -4.0345 |
| sortino_ratio | -0.8466 |
| max_drawdown | 0.6382 |
| cagr | -0.3259 |
| net_avg_win | 45.3516 |
| net_avg_loss | -79.2188 |
| avg_hold_time_bars | 6.1878 |
| exposure | 0.0599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

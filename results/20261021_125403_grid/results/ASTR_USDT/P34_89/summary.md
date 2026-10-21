# EMA Hourly Continuation — ASTR/USDT P34_89

**Symbol:** ASTR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.7561 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0512 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -1.9086 |
| sortino_ratio | -0.5700 |
| max_drawdown | 0.4995 |
| cagr | -0.2314 |
| net_avg_win | 67.4309 |
| net_avg_loss | -93.3734 |
| avg_hold_time_bars | 12.8830 |
| exposure | 0.2542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

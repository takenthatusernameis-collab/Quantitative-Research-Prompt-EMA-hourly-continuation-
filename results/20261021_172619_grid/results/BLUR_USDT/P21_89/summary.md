# EMA Hourly Continuation — BLUR/USDT P21_89

**Symbol:** BLUR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.8675 |
| net_win_rate | 0.5214 |
| gross_profit_factor | 1.0945 |
| gross_win_rate | 0.5214 |
| sharpe_ratio | -1.0604 |
| sortino_ratio | -0.3371 |
| max_drawdown | 0.4578 |
| cagr | -0.1464 |
| net_avg_win | 84.1781 |
| net_avg_loss | -105.7124 |
| avg_hold_time_bars | 17.2525 |
| exposure | 0.3833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

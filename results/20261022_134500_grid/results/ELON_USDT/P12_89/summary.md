# EMA Hourly Continuation — ELON/USDT P12_89

**Symbol:** ELON/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 803 |
| net_profit_factor | 0.5491 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.8340 |
| gross_win_rate | 0.4558 |
| sharpe_ratio | -5.4014 |
| sortino_ratio | -2.1555 |
| max_drawdown | 0.9257 |
| cagr | -0.6428 |
| net_avg_win | 31.0140 |
| net_avg_loss | -46.6012 |
| avg_hold_time_bars | 13.5243 |
| exposure | 0.4936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

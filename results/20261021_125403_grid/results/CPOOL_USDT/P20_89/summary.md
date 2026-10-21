# EMA Hourly Continuation — CPOOL/USDT P20_89

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.8742 |
| net_win_rate | 0.5098 |
| gross_profit_factor | 1.0262 |
| gross_win_rate | 0.5098 |
| sharpe_ratio | -0.8951 |
| sortino_ratio | -0.2905 |
| max_drawdown | 0.3395 |
| cagr | -0.1292 |
| net_avg_win | 78.1501 |
| net_avg_loss | -92.9567 |
| avg_hold_time_bars | 13.7402 |
| exposure | 0.3198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

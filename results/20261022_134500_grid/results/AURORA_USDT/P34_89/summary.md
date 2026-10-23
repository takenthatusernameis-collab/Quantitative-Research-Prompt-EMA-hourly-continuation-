# EMA Hourly Continuation — AURORA/USDT P34_89

**Symbol:** AURORA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.5253 |
| net_win_rate | 0.4381 |
| gross_profit_factor | 0.9291 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -5.7450 |
| sortino_ratio | -1.8883 |
| max_drawdown | 0.9126 |
| cagr | -0.6163 |
| net_avg_win | 41.2664 |
| net_avg_loss | -61.2367 |
| avg_hold_time_bars | 10.4039 |
| exposure | 0.2634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

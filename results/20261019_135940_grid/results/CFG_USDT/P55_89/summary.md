# EMA Hourly Continuation — CFG/USDT P55_89

**Symbol:** CFG/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.4670 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.8008 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -5.8807 |
| sortino_ratio | -2.2110 |
| max_drawdown | 0.9328 |
| cagr | -0.6535 |
| net_avg_win | 26.2049 |
| net_avg_loss | -44.0692 |
| avg_hold_time_bars | 3.9279 |
| exposure | 0.1262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

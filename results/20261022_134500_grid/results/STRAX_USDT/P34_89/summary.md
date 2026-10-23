# EMA Hourly Continuation — STRAX/USDT P34_89

**Symbol:** STRAX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 751 |
| net_profit_factor | 0.4865 |
| net_win_rate | 0.4141 |
| gross_profit_factor | 0.7995 |
| gross_win_rate | 0.4274 |
| sharpe_ratio | -7.4342 |
| sortino_ratio | -2.8709 |
| max_drawdown | 0.9715 |
| cagr | -0.7596 |
| net_avg_win | 29.5970 |
| net_avg_loss | -43.0001 |
| avg_hold_time_bars | 7.8016 |
| exposure | 0.2679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ARKM/USDT P55_89

**Symbol:** ARKM/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.5363 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9235 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -5.0532 |
| sortino_ratio | -1.8576 |
| max_drawdown | 0.8981 |
| cagr | -0.5959 |
| net_avg_win | 31.9269 |
| net_avg_loss | -54.1980 |
| avg_hold_time_bars | 3.9164 |
| exposure | 0.1214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — IO/USDT P26_144

**Symbol:** IO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.6472 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.8736 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -3.3533 |
| sortino_ratio | -1.0903 |
| max_drawdown | 0.7220 |
| cagr | -0.4113 |
| net_avg_win | 55.4488 |
| net_avg_loss | -74.0625 |
| avg_hold_time_bars | 17.8271 |
| exposure | 0.4393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

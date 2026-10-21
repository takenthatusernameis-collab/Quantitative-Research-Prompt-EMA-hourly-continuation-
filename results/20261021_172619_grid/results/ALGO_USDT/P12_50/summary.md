# EMA Hourly Continuation — ALGO/USDT P12_50

**Symbol:** ALGO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.8318 |
| net_win_rate | 0.5237 |
| gross_profit_factor | 1.0810 |
| gross_win_rate | 0.5237 |
| sharpe_ratio | -1.3157 |
| sortino_ratio | -0.4688 |
| max_drawdown | 0.4527 |
| cagr | -0.1956 |
| net_avg_win | 65.1000 |
| net_avg_loss | -86.0609 |
| avg_hold_time_bars | 11.4484 |
| exposure | 0.3180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

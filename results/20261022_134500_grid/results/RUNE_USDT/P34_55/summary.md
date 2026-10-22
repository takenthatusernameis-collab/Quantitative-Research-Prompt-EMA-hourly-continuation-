# EMA Hourly Continuation — RUNE/USDT P34_55

**Symbol:** RUNE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 851 |
| net_profit_factor | 0.4806 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.9704 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -7.3392 |
| sortino_ratio | -3.0019 |
| max_drawdown | 0.9794 |
| cagr | -0.7837 |
| net_avg_win | 22.5842 |
| net_avg_loss | -41.8719 |
| avg_hold_time_bars | 3.4653 |
| exposure | 0.1340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

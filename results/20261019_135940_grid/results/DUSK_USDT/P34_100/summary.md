# EMA Hourly Continuation — DUSK/USDT P34_100

**Symbol:** DUSK/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.6230 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.9381 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -3.9065 |
| sortino_ratio | -1.3922 |
| max_drawdown | 0.8181 |
| cagr | -0.4837 |
| net_avg_win | 44.7661 |
| net_avg_loss | -63.1889 |
| avg_hold_time_bars | 9.6432 |
| exposure | 0.2801 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

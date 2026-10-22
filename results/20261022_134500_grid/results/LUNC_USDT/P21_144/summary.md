# EMA Hourly Continuation — LUNC/USDT P21_144

**Symbol:** LUNC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.6082 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 0.9333 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -3.8031 |
| sortino_ratio | -1.3281 |
| max_drawdown | 0.8065 |
| cagr | -0.4698 |
| net_avg_win | 41.6361 |
| net_avg_loss | -64.3467 |
| avg_hold_time_bars | 17.0114 |
| exposure | 0.4740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

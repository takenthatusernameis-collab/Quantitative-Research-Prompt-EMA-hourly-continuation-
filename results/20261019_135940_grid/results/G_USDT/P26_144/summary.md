# EMA Hourly Continuation — G/USDT P26_144

**Symbol:** G/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.5203 |
| net_win_rate | 0.4268 |
| gross_profit_factor | 0.7813 |
| gross_win_rate | 0.4341 |
| sharpe_ratio | -4.4689 |
| sortino_ratio | -1.3564 |
| max_drawdown | 0.7841 |
| cagr | -0.4828 |
| net_avg_win | 47.1699 |
| net_avg_loss | -67.5098 |
| avg_hold_time_bars | 23.9902 |
| exposure | 0.5172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — T/USDT P89_144

**Symbol:** T/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.4792 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.8871 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -4.6812 |
| sortino_ratio | -1.4178 |
| max_drawdown | 0.8329 |
| cagr | -0.5017 |
| net_avg_win | 35.7426 |
| net_avg_loss | -63.2964 |
| avg_hold_time_bars | 7.1207 |
| exposure | 0.1495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

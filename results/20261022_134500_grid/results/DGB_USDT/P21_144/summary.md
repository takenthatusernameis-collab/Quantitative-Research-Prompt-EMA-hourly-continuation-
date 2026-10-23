# EMA Hourly Continuation — DGB/USDT P21_144

**Symbol:** DGB/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.6004 |
| net_win_rate | 0.4486 |
| gross_profit_factor | 0.8946 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -4.5566 |
| sortino_ratio | -1.5850 |
| max_drawdown | 0.8622 |
| cagr | -0.5335 |
| net_avg_win | 46.5773 |
| net_avg_loss | -63.1224 |
| avg_hold_time_bars | 18.6868 |
| exposure | 0.5207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — RLC/USDT P34_144

**Symbol:** RLC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.5883 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.8682 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -3.8889 |
| sortino_ratio | -1.2533 |
| max_drawdown | 0.7863 |
| cagr | -0.4522 |
| net_avg_win | 46.2096 |
| net_avg_loss | -66.6566 |
| avg_hold_time_bars | 16.9295 |
| exposure | 0.4040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

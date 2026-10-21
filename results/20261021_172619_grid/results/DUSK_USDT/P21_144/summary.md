# EMA Hourly Continuation — DUSK/USDT P21_144

**Symbol:** DUSK/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.8362 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9706 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -1.0739 |
| sortino_ratio | -0.2966 |
| max_drawdown | 0.3641 |
| cagr | -0.1293 |
| net_avg_win | 81.4837 |
| net_avg_loss | -94.3648 |
| avg_hold_time_bars | 29.6818 |
| exposure | 0.5046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

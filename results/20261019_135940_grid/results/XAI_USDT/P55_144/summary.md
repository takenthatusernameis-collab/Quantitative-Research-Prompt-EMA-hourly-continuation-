# EMA Hourly Continuation — XAI/USDT P55_144

**Symbol:** XAI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.6413 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.9160 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -3.3533 |
| sortino_ratio | -1.0545 |
| max_drawdown | 0.7333 |
| cagr | -0.3944 |
| net_avg_win | 54.9460 |
| net_avg_loss | -75.3355 |
| avg_hold_time_bars | 13.2129 |
| exposure | 0.2991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — AURORA/USDT P20_50

**Symbol:** AURORA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 787 |
| net_profit_factor | 0.4136 |
| net_win_rate | 0.4028 |
| gross_profit_factor | 0.8255 |
| gross_win_rate | 0.4257 |
| sharpe_ratio | -8.3927 |
| sortino_ratio | -3.3306 |
| max_drawdown | 0.9861 |
| cagr | -0.8133 |
| net_avg_win | 21.9241 |
| net_avg_loss | -35.7491 |
| avg_hold_time_bars | 6.8272 |
| exposure | 0.2442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

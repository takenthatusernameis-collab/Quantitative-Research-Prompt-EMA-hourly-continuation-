# EMA Hourly Continuation — VELO/USDT P12_50

**Symbol:** VELO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1177 |
| net_profit_factor | 0.5856 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.8563 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -5.7196 |
| sortino_ratio | -2.7507 |
| max_drawdown | 0.9674 |
| cagr | -0.7358 |
| net_avg_win | 24.6516 |
| net_avg_loss | -37.3060 |
| avg_hold_time_bars | 5.8785 |
| exposure | 0.3145 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

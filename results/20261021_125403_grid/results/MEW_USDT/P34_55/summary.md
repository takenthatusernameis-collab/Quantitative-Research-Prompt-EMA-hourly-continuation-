# EMA Hourly Continuation — MEW/USDT P34_55

**Symbol:** MEW/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.6614 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8916 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -2.6858 |
| sortino_ratio | -0.7363 |
| max_drawdown | 0.5765 |
| cagr | -0.2871 |
| net_avg_win | 65.0154 |
| net_avg_loss | -85.8246 |
| avg_hold_time_bars | 4.9946 |
| exposure | 0.0838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

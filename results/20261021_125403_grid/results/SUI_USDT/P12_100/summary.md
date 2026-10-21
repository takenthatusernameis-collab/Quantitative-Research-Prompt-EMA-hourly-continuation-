# EMA Hourly Continuation — SUI/USDT P12_100

**Symbol:** SUI/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.9525 |
| net_win_rate | 0.5333 |
| gross_profit_factor | 1.1355 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -0.2721 |
| sortino_ratio | -0.0806 |
| max_drawdown | 0.2668 |
| cagr | -0.0426 |
| net_avg_win | 92.8022 |
| net_avg_loss | -111.3463 |
| avg_hold_time_bars | 29.9762 |
| exposure | 0.5723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

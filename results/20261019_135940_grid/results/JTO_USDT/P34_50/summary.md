# EMA Hourly Continuation — JTO/USDT P34_50

**Symbol:** JTO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 895 |
| net_profit_factor | 0.4741 |
| net_win_rate | 0.4503 |
| gross_profit_factor | 0.8910 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -7.0392 |
| sortino_ratio | -2.9908 |
| max_drawdown | 0.9734 |
| cagr | -0.7627 |
| net_avg_win | 21.7624 |
| net_avg_loss | -37.6025 |
| avg_hold_time_bars | 3.1073 |
| exposure | 0.1264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ROSE/USDT P34_50

**Symbol:** ROSE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.4707 |
| net_win_rate | 0.4437 |
| gross_profit_factor | 0.9518 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -8.2330 |
| sortino_ratio | -3.5965 |
| max_drawdown | 0.9893 |
| cagr | -0.8333 |
| net_avg_win | 20.8400 |
| net_avg_loss | -35.3180 |
| avg_hold_time_bars | 2.6278 |
| exposure | 0.1136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

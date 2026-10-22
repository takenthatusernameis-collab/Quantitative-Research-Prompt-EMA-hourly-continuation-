# EMA Hourly Continuation — SUI/USDT P50_200

**Symbol:** SUI/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6736 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 0.9612 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -2.4538 |
| sortino_ratio | -0.7014 |
| max_drawdown | 0.6077 |
| cagr | -0.2833 |
| net_avg_win | 57.8913 |
| net_avg_loss | -83.8720 |
| avg_hold_time_bars | 18.7384 |
| exposure | 0.3484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

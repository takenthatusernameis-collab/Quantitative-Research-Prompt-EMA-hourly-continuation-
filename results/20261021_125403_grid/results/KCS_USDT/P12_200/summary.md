# EMA Hourly Continuation — KCS/USDT P12_200

**Symbol:** KCS/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.6398 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9598 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -2.7055 |
| sortino_ratio | -0.6948 |
| max_drawdown | 0.5594 |
| cagr | -0.2739 |
| net_avg_win | 63.3087 |
| net_avg_loss | -90.7496 |
| avg_hold_time_bars | 46.6358 |
| exposure | 0.6868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

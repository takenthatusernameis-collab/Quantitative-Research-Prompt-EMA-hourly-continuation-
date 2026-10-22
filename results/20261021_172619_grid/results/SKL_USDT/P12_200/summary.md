# EMA Hourly Continuation — SKL/USDT P12_200

**Symbol:** SKL/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.8790 |
| net_win_rate | 0.5096 |
| gross_profit_factor | 1.0272 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -0.7027 |
| sortino_ratio | -0.1784 |
| max_drawdown | 0.3451 |
| cagr | -0.0813 |
| net_avg_win | 87.0762 |
| net_avg_loss | -102.9193 |
| avg_hold_time_bars | 51.0159 |
| exposure | 0.7281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

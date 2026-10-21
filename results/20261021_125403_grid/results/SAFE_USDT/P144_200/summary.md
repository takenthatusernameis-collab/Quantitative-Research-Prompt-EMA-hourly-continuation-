# EMA Hourly Continuation — SAFE/USDT P144_200

**Symbol:** SAFE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 200 |
| net_profit_factor | 0.5868 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.7986 |
| gross_win_rate | 0.4450 |
| sharpe_ratio | -2.3108 |
| sortino_ratio | -0.4669 |
| max_drawdown | 0.4163 |
| cagr | -0.1926 |
| net_avg_win | 65.9440 |
| net_avg_loss | -90.1109 |
| avg_hold_time_bars | 11.9150 |
| exposure | 0.1091 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

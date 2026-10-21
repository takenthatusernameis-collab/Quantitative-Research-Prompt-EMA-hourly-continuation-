# EMA Hourly Continuation — MINA/USDT P20_200

**Symbol:** MINA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.8839 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0639 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -0.5964 |
| sortino_ratio | -0.1542 |
| max_drawdown | 0.2912 |
| cagr | -0.0719 |
| net_avg_win | 76.9558 |
| net_avg_loss | -94.9244 |
| avg_hold_time_bars | 43.8117 |
| exposure | 0.6452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

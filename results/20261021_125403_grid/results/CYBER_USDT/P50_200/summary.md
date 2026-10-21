# EMA Hourly Continuation — CYBER/USDT P50_200

**Symbol:** CYBER/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.8400 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0298 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -0.8591 |
| sortino_ratio | -0.2171 |
| max_drawdown | 0.2854 |
| cagr | -0.0969 |
| net_avg_win | 74.5865 |
| net_avg_loss | -93.4930 |
| avg_hold_time_bars | 27.4484 |
| exposure | 0.3868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

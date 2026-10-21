# EMA Hourly Continuation — ADA/USDT P20_21

**Symbol:** ADA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 105 |
| net_profit_factor | 0.9486 |
| net_win_rate | 0.5714 |
| gross_profit_factor | 1.3214 |
| gross_win_rate | 0.5714 |
| sharpe_ratio | -0.1423 |
| sortino_ratio | -0.0213 |
| max_drawdown | 0.1185 |
| cagr | -0.0112 |
| net_avg_win | 85.6458 |
| net_avg_loss | -120.3832 |
| avg_hold_time_bars | 4.0952 |
| exposure | 0.0195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

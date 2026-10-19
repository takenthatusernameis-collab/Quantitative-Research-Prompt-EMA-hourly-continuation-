# EMA Hourly Continuation — ZEC/USDT P89_100

**Symbol:** ZEC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 587 |
| net_profit_factor | 0.2282 |
| net_win_rate | 0.3935 |
| gross_profit_factor | 0.7092 |
| gross_win_rate | 0.4208 |
| sharpe_ratio | -8.5348 |
| sortino_ratio | -2.9745 |
| max_drawdown | 0.9785 |
| cagr | -0.7813 |
| net_avg_win | 12.5214 |
| net_avg_loss | -35.5971 |
| avg_hold_time_bars | 1.9506 |
| exposure | 0.0520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

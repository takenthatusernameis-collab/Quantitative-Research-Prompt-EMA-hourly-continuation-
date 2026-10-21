# EMA Hourly Continuation — CTC/USDT P20_100

**Symbol:** CTC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.8000 |
| net_win_rate | 0.5166 |
| gross_profit_factor | 1.0480 |
| gross_win_rate | 0.5166 |
| sharpe_ratio | -1.4972 |
| sortino_ratio | -0.4870 |
| max_drawdown | 0.4868 |
| cagr | -0.2023 |
| net_avg_win | 65.3907 |
| net_avg_loss | -87.3411 |
| avg_hold_time_bars | 17.0448 |
| exposure | 0.3975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

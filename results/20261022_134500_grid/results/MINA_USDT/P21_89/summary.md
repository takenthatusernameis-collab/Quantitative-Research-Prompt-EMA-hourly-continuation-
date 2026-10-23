# EMA Hourly Continuation — MINA/USDT P21_89

**Symbol:** MINA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.6487 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9905 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -3.3791 |
| sortino_ratio | -1.2189 |
| max_drawdown | 0.8073 |
| cagr | -0.4458 |
| net_avg_win | 43.5040 |
| net_avg_loss | -65.8626 |
| avg_hold_time_bars | 14.1737 |
| exposure | 0.4265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — QI/USDT P34_144

**Symbol:** QI/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7460 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 0.9539 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -1.7159 |
| sortino_ratio | -0.4712 |
| max_drawdown | 0.4387 |
| cagr | -0.1951 |
| net_avg_win | 68.3978 |
| net_avg_loss | -87.3450 |
| avg_hold_time_bars | 20.8544 |
| exposure | 0.3501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

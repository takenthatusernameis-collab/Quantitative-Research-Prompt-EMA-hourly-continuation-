# EMA Hourly Continuation — LUNC/USDT P55_89

**Symbol:** LUNC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.4167 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.8815 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -6.7792 |
| sortino_ratio | -2.5838 |
| max_drawdown | 0.9621 |
| cagr | -0.7249 |
| net_avg_win | 20.1914 |
| net_avg_loss | -42.7892 |
| avg_hold_time_bars | 3.8510 |
| exposure | 0.1269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

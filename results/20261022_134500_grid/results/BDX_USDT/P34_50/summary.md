# EMA Hourly Continuation — BDX/USDT P34_50

**Symbol:** BDX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1366 |
| net_profit_factor | 0.1653 |
| net_win_rate | 0.2028 |
| gross_profit_factor | 0.6038 |
| gross_win_rate | 0.2965 |
| sharpe_ratio | -23.0566 |
| sortino_ratio | -13.9160 |
| max_drawdown | 1.0000 |
| cagr | -0.9996 |
| net_avg_win | 7.1513 |
| net_avg_loss | -11.0017 |
| avg_hold_time_bars | 2.0037 |
| exposure | 0.1244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

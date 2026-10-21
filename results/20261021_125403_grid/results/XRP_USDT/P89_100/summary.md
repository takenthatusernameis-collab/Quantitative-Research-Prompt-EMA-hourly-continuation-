# EMA Hourly Continuation — XRP/USDT P89_100

**Symbol:** XRP/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 68 |
| net_profit_factor | 0.7806 |
| net_win_rate | 0.5735 |
| gross_profit_factor | 1.3339 |
| gross_win_rate | 0.5735 |
| sharpe_ratio | -0.5905 |
| sortino_ratio | -0.0710 |
| max_drawdown | 0.0949 |
| cagr | -0.0316 |
| net_avg_win | 70.6355 |
| net_avg_loss | -121.6906 |
| avg_hold_time_bars | 6.9853 |
| exposure | 0.0216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

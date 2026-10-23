# EMA Hourly Continuation — CTC/USDT P34_200

**Symbol:** CTC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.6509 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 1.0349 |
| gross_win_rate | 0.5054 |
| sharpe_ratio | -3.1124 |
| sortino_ratio | -0.9304 |
| max_drawdown | 0.7143 |
| cagr | -0.3668 |
| net_avg_win | 56.8104 |
| net_avg_loss | -83.1971 |
| avg_hold_time_bars | 21.3791 |
| exposure | 0.4460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

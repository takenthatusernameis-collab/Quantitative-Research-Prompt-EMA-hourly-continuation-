# EMA Hourly Continuation — XEC/USDT P26_144

**Symbol:** XEC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.6660 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9922 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -3.3099 |
| sortino_ratio | -1.0960 |
| max_drawdown | 0.7457 |
| cagr | -0.4055 |
| net_avg_win | 55.3950 |
| net_avg_loss | -75.6929 |
| avg_hold_time_bars | 19.5399 |
| exposure | 0.4881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

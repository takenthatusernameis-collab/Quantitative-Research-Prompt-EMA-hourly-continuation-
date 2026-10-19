# EMA Hourly Continuation — CFX/USDT P34_144

**Symbol:** CFX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.6516 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9501 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -2.8397 |
| sortino_ratio | -0.8594 |
| max_drawdown | 0.6501 |
| cagr | -0.3338 |
| net_avg_win | 53.3749 |
| net_avg_loss | -77.4252 |
| avg_hold_time_bars | 19.1996 |
| exposure | 0.4023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CFX/USDT P34_144

**Symbol:** CFX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.7759 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 0.9644 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -1.4346 |
| sortino_ratio | -0.3779 |
| max_drawdown | 0.3736 |
| cagr | -0.1599 |
| net_avg_win | 73.0338 |
| net_avg_loss | -91.9375 |
| avg_hold_time_bars | 25.4029 |
| exposure | 0.3926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

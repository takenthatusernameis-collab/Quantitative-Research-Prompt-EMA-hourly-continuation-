# EMA Hourly Continuation — WIN/USDT P34_200

**Symbol:** WIN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.7125 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9155 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -1.6096 |
| sortino_ratio | -0.3753 |
| max_drawdown | 0.4211 |
| cagr | -0.1591 |
| net_avg_win | 67.7786 |
| net_avg_loss | -88.9286 |
| avg_hold_time_bars | 40.2734 |
| exposure | 0.4888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

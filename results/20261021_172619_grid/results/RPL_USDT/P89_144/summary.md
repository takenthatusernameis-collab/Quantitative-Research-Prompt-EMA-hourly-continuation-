# EMA Hourly Continuation — RPL/USDT P89_144

**Symbol:** RPL/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.7590 |
| net_win_rate | 0.5096 |
| gross_profit_factor | 1.0301 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -1.4957 |
| sortino_ratio | -0.3786 |
| max_drawdown | 0.3800 |
| cagr | -0.1593 |
| net_avg_win | 70.1858 |
| net_avg_loss | -96.1003 |
| avg_hold_time_bars | 9.2019 |
| exposure | 0.1299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

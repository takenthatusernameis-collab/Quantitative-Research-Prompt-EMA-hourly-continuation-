# EMA Hourly Continuation — ETN/USDT P8_34

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.4655 |
| net_win_rate | 0.3954 |
| gross_profit_factor | 0.5894 |
| gross_win_rate | 0.3954 |
| sharpe_ratio | -5.4884 |
| sortino_ratio | -2.0096 |
| max_drawdown | 0.8640 |
| cagr | -0.6061 |
| net_avg_win | 33.5413 |
| net_avg_loss | -47.1212 |
| avg_hold_time_bars | 8.7163 |
| exposure | 0.2670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

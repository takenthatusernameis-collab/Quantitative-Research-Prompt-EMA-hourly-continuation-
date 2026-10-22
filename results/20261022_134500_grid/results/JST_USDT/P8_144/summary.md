# EMA Hourly Continuation — JST/USDT P8_144

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.5458 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9966 |
| gross_win_rate | 0.5023 |
| sharpe_ratio | -3.5487 |
| sortino_ratio | -1.0141 |
| max_drawdown | 0.7384 |
| cagr | -0.4027 |
| net_avg_win | 42.0282 |
| net_avg_loss | -70.8707 |
| avg_hold_time_bars | 37.8088 |
| exposure | 0.7425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

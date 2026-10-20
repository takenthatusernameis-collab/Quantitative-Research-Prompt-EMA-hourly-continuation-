# EMA Hourly Continuation — SSV/USDT P100_144

**Symbol:** SSV/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.4448 |
| net_win_rate | 0.4183 |
| gross_profit_factor | 0.7884 |
| gross_win_rate | 0.4345 |
| sharpe_ratio | -6.2400 |
| sortino_ratio | -2.0914 |
| max_drawdown | 0.9236 |
| cagr | -0.6370 |
| net_avg_win | 31.7139 |
| net_avg_loss | -51.2760 |
| avg_hold_time_bars | 3.8528 |
| exposure | 0.0971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

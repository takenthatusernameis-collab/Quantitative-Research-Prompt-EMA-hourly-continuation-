# EMA Hourly Continuation — BTT/USDT P55_144

**Symbol:** BTT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.5097 |
| net_win_rate | 0.4390 |
| gross_profit_factor | 0.8248 |
| gross_win_rate | 0.4390 |
| sharpe_ratio | -4.2633 |
| sortino_ratio | -1.1050 |
| max_drawdown | 0.7312 |
| cagr | -0.4074 |
| net_avg_win | 52.7911 |
| net_avg_loss | -81.0548 |
| avg_hold_time_bars | 18.2713 |
| exposure | 0.2724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

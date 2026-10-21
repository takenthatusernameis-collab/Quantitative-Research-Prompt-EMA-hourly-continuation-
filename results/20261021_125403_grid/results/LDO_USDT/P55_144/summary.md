# EMA Hourly Continuation — LDO/USDT P55_144

**Symbol:** LDO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.7356 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.8931 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -1.7887 |
| sortino_ratio | -0.4605 |
| max_drawdown | 0.4405 |
| cagr | -0.1910 |
| net_avg_win | 74.0804 |
| net_avg_loss | -90.2333 |
| avg_hold_time_bars | 17.5549 |
| exposure | 0.2617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

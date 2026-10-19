# EMA Hourly Continuation — BONK/USDT P12_34

**Symbol:** BONK/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1260 |
| net_profit_factor | 0.5740 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.9329 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -7.7033 |
| sortino_ratio | -3.8368 |
| max_drawdown | 0.9914 |
| cagr | -0.8482 |
| net_avg_win | 23.6375 |
| net_avg_loss | -33.4780 |
| avg_hold_time_bars | 4.1722 |
| exposure | 0.2390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

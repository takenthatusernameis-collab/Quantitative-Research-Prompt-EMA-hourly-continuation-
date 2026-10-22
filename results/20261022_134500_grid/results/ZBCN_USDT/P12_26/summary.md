# EMA Hourly Continuation — ZBCN/USDT P12_26

**Symbol:** ZBCN/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1528 |
| net_profit_factor | 0.4224 |
| net_win_rate | 0.4483 |
| gross_profit_factor | 0.7667 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -9.5713 |
| sortino_ratio | -5.3099 |
| max_drawdown | 0.9986 |
| cagr | -0.9290 |
| net_avg_win | 10.6606 |
| net_avg_loss | -20.5075 |
| avg_hold_time_bars | 2.6420 |
| exposure | 0.1868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

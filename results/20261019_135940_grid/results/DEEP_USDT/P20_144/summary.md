# EMA Hourly Continuation — DEEP/USDT P20_144

**Symbol:** DEEP/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.7113 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9088 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -2.0201 |
| sortino_ratio | -0.5663 |
| max_drawdown | 0.4184 |
| cagr | -0.2345 |
| net_avg_win | 67.5201 |
| net_avg_loss | -87.4424 |
| avg_hold_time_bars | 34.3375 |
| exposure | 0.6163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

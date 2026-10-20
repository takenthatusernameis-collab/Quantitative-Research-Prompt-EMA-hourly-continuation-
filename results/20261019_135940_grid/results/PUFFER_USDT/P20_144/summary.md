# EMA Hourly Continuation — PUFFER/USDT P20_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.8163 |
| net_win_rate | 0.5217 |
| gross_profit_factor | 1.0981 |
| gross_win_rate | 0.5243 |
| sharpe_ratio | -1.2887 |
| sortino_ratio | -0.3987 |
| max_drawdown | 0.4182 |
| cagr | -0.1790 |
| net_avg_win | 71.5063 |
| net_avg_loss | -95.5637 |
| avg_hold_time_bars | 24.8824 |
| exposure | 0.5506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

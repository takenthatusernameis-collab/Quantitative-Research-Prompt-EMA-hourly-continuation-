# EMA Hourly Continuation — ROSE/USDT P34_144

**Symbol:** ROSE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.9117 |
| net_win_rate | 0.5263 |
| gross_profit_factor | 1.0979 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -0.5161 |
| sortino_ratio | -0.1412 |
| max_drawdown | 0.2543 |
| cagr | -0.0666 |
| net_avg_win | 86.3696 |
| net_avg_loss | -105.2598 |
| avg_hold_time_bars | 25.2161 |
| exposure | 0.4138 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ZBCN/USDT P100_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.4809 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.8188 |
| gross_win_rate | 0.4566 |
| sharpe_ratio | -5.1605 |
| sortino_ratio | -1.7592 |
| max_drawdown | 0.8826 |
| cagr | -0.5764 |
| net_avg_win | 31.3464 |
| net_avg_loss | -53.6350 |
| avg_hold_time_bars | 3.4167 |
| exposure | 0.0911 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — RENDER/USDT P100_144

**Symbol:** RENDER/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 191 |
| net_profit_factor | 0.8963 |
| net_win_rate | 0.5393 |
| gross_profit_factor | 1.1636 |
| gross_win_rate | 0.5393 |
| sharpe_ratio | -0.4921 |
| sortino_ratio | -0.1060 |
| max_drawdown | 0.1807 |
| cagr | -0.0497 |
| net_avg_win | 87.5476 |
| net_avg_loss | -114.3221 |
| avg_hold_time_bars | 7.1990 |
| exposure | 0.0726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

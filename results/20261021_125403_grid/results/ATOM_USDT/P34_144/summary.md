# EMA Hourly Continuation — ATOM/USDT P34_144

**Symbol:** ATOM/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.8166 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0386 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -0.9947 |
| sortino_ratio | -0.2668 |
| max_drawdown | 0.3477 |
| cagr | -0.1174 |
| net_avg_win | 66.5739 |
| net_avg_loss | -87.3472 |
| avg_hold_time_bars | 25.0460 |
| exposure | 0.3962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

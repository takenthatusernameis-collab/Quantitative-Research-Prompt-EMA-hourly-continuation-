# EMA Hourly Continuation — PROM/USDT P21_144

**Symbol:** PROM/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.5437 |
| net_win_rate | 0.4204 |
| gross_profit_factor | 0.7273 |
| gross_win_rate | 0.4276 |
| sharpe_ratio | -3.8007 |
| sortino_ratio | -1.0985 |
| max_drawdown | 0.7348 |
| cagr | -0.4017 |
| net_avg_win | 48.7922 |
| net_avg_loss | -65.0964 |
| avg_hold_time_bars | 24.9406 |
| exposure | 0.4773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

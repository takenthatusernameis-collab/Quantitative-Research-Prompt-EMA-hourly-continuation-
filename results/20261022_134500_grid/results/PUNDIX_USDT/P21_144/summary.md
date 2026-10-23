# EMA Hourly Continuation — PUNDIX/USDT P21_144

**Symbol:** PUNDIX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.5438 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.8430 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -3.7562 |
| sortino_ratio | -1.1912 |
| max_drawdown | 0.7713 |
| cagr | -0.4387 |
| net_avg_win | 38.1764 |
| net_avg_loss | -61.2366 |
| avg_hold_time_bars | 23.5127 |
| exposure | 0.5483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

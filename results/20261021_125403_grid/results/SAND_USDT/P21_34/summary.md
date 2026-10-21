# EMA Hourly Continuation — SAND/USDT P21_34

**Symbol:** SAND/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.6398 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9367 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -2.3194 |
| sortino_ratio | -0.5507 |
| max_drawdown | 0.5088 |
| cagr | -0.2226 |
| net_avg_win | 63.0663 |
| net_avg_loss | -91.6346 |
| avg_hold_time_bars | 4.9635 |
| exposure | 0.0618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

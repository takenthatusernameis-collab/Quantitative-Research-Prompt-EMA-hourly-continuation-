# EMA Hourly Continuation — EGLD/USDT P8_89

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.8835 |
| net_win_rate | 0.5269 |
| gross_profit_factor | 1.1151 |
| gross_win_rate | 0.5269 |
| sharpe_ratio | -0.9369 |
| sortino_ratio | -0.3135 |
| max_drawdown | 0.4438 |
| cagr | -0.1377 |
| net_avg_win | 82.9746 |
| net_avg_loss | -104.5911 |
| avg_hold_time_bars | 25.2208 |
| exposure | 0.6179 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

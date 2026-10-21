# EMA Hourly Continuation — OP/USDT P8_12

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.7885 |
| net_win_rate | 0.5261 |
| gross_profit_factor | 1.0913 |
| gross_win_rate | 0.5261 |
| sharpe_ratio | -1.0461 |
| sortino_ratio | -0.2291 |
| max_drawdown | 0.2577 |
| cagr | -0.0999 |
| net_avg_win | 71.5739 |
| net_avg_loss | -100.7618 |
| avg_hold_time_bars | 4.4217 |
| exposure | 0.0462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

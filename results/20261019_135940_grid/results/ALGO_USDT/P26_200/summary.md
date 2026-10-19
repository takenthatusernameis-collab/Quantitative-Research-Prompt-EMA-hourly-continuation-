# EMA Hourly Continuation — ALGO/USDT P26_200

**Symbol:** ALGO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.7814 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0926 |
| gross_win_rate | 0.5274 |
| sharpe_ratio | -1.3219 |
| sortino_ratio | -0.3442 |
| max_drawdown | 0.3579 |
| cagr | -0.1556 |
| net_avg_win | 68.3438 |
| net_avg_loss | -95.3618 |
| avg_hold_time_bars | 37.5072 |
| exposure | 0.5916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

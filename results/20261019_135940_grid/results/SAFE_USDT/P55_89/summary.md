# EMA Hourly Continuation — SAFE/USDT P55_89

**Symbol:** SAFE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.5172 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.9203 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -5.2217 |
| sortino_ratio | -1.8461 |
| max_drawdown | 0.8991 |
| cagr | -0.5898 |
| net_avg_win | 33.1618 |
| net_avg_loss | -55.4533 |
| avg_hold_time_bars | 5.6747 |
| exposure | 0.1614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CSPR/USDT P26_89

**Symbol:** CSPR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7618 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 0.9525 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -1.8245 |
| sortino_ratio | -0.5702 |
| max_drawdown | 0.4972 |
| cagr | -0.2313 |
| net_avg_win | 66.0798 |
| net_avg_loss | -83.1830 |
| avg_hold_time_bars | 11.3912 |
| exposure | 0.2475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

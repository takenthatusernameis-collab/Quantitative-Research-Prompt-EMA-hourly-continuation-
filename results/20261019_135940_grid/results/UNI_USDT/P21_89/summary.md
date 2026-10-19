# EMA Hourly Continuation — UNI/USDT P21_89

**Symbol:** UNI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.6271 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9618 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -4.1252 |
| sortino_ratio | -1.5430 |
| max_drawdown | 0.8514 |
| cagr | -0.5238 |
| net_avg_win | 41.5446 |
| net_avg_loss | -62.0732 |
| avg_hold_time_bars | 11.3352 |
| exposure | 0.3643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

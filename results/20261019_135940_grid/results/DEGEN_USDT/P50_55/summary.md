# EMA Hourly Continuation — DEGEN/USDT P50_55

**Symbol:** DEGEN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 799 |
| net_profit_factor | 0.3503 |
| net_win_rate | 0.3529 |
| gross_profit_factor | 0.7034 |
| gross_win_rate | 0.3992 |
| sharpe_ratio | -10.9460 |
| sortino_ratio | -4.4414 |
| max_drawdown | 0.9972 |
| cagr | -0.9039 |
| net_avg_win | 19.0692 |
| net_avg_loss | -29.6892 |
| avg_hold_time_bars | 2.1790 |
| exposure | 0.0793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

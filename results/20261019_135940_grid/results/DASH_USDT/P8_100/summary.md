# EMA Hourly Continuation — DASH/USDT P8_100

**Symbol:** DASH/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.5449 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.9099 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -4.6941 |
| sortino_ratio | -1.7164 |
| max_drawdown | 0.8805 |
| cagr | -0.5646 |
| net_avg_win | 33.2977 |
| net_avg_loss | -52.7386 |
| avg_hold_time_bars | 21.7750 |
| exposure | 0.6730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ALEX/USDT P26_100

**Symbol:** ALEX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.5581 |
| net_win_rate | 0.4119 |
| gross_profit_factor | 0.8173 |
| gross_win_rate | 0.4137 |
| sharpe_ratio | -5.2129 |
| sortino_ratio | -1.6891 |
| max_drawdown | 0.8846 |
| cagr | -0.5609 |
| net_avg_win | 49.6969 |
| net_avg_loss | -62.3555 |
| avg_hold_time_bars | 16.7848 |
| exposure | 0.4112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

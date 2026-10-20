# EMA Hourly Continuation — CHR/USDT P89_100

**Symbol:** CHR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.3817 |
| net_win_rate | 0.4310 |
| gross_profit_factor | 0.9036 |
| gross_win_rate | 0.4514 |
| sharpe_ratio | -7.8423 |
| sortino_ratio | -2.8211 |
| max_drawdown | 0.9737 |
| cagr | -0.7628 |
| net_avg_win | 21.8575 |
| net_avg_loss | -43.3765 |
| avg_hold_time_bars | 2.5235 |
| exposure | 0.0729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

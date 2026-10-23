# EMA Hourly Continuation — DODO/USDT P50_55

**Symbol:** DODO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 895 |
| net_profit_factor | 0.2835 |
| net_win_rate | 0.3374 |
| gross_profit_factor | 0.8379 |
| gross_win_rate | 0.4022 |
| sharpe_ratio | -12.6913 |
| sortino_ratio | -5.5161 |
| max_drawdown | 0.9994 |
| cagr | -0.9459 |
| net_avg_win | 13.0911 |
| net_avg_loss | -23.5196 |
| avg_hold_time_bars | 2.2413 |
| exposure | 0.0908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

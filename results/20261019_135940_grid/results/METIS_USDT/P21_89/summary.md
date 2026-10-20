# EMA Hourly Continuation — METIS/USDT P21_89

**Symbol:** METIS/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.5369 |
| net_win_rate | 0.4388 |
| gross_profit_factor | 0.8180 |
| gross_win_rate | 0.4415 |
| sharpe_ratio | -5.5330 |
| sortino_ratio | -2.0954 |
| max_drawdown | 0.9237 |
| cagr | -0.6358 |
| net_avg_win | 33.4645 |
| net_avg_loss | -48.7345 |
| avg_hold_time_bars | 10.8982 |
| exposure | 0.3601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

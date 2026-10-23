# EMA Hourly Continuation — BLUR/USDT P20_50

**Symbol:** BLUR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 970 |
| net_profit_factor | 0.5703 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.9784 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -6.2060 |
| sortino_ratio | -2.6969 |
| max_drawdown | 0.9670 |
| cagr | -0.7346 |
| net_avg_win | 28.0790 |
| net_avg_loss | -43.6808 |
| avg_hold_time_bars | 5.0876 |
| exposure | 0.2233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — AVAX/USDT P21_100

**Symbol:** AVAX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.8388 |
| net_win_rate | 0.5113 |
| gross_profit_factor | 1.0612 |
| gross_win_rate | 0.5113 |
| sharpe_ratio | -1.3174 |
| sortino_ratio | -0.3973 |
| max_drawdown | 0.4443 |
| cagr | -0.1686 |
| net_avg_win | 85.4430 |
| net_avg_loss | -106.5739 |
| avg_hold_time_bars | 18.0475 |
| exposure | 0.3626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

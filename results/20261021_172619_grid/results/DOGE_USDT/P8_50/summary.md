# EMA Hourly Continuation — DOGE/USDT P8_50

**Symbol:** DOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.7498 |
| net_win_rate | 0.4971 |
| gross_profit_factor | 0.9818 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -2.3489 |
| sortino_ratio | -0.8786 |
| max_drawdown | 0.6473 |
| cagr | -0.3324 |
| net_avg_win | 56.3480 |
| net_avg_loss | -74.2770 |
| avg_hold_time_bars | 11.8842 |
| exposure | 0.3684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

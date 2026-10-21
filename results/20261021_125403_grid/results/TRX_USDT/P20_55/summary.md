# EMA Hourly Continuation — TRX/USDT P20_55

**Symbol:** TRX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.4355 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9353 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -5.1827 |
| sortino_ratio | -1.5658 |
| max_drawdown | 0.8415 |
| cagr | -0.5113 |
| net_avg_win | 31.4058 |
| net_avg_loss | -65.9918 |
| avg_hold_time_bars | 9.3473 |
| exposure | 0.1823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — NOT/USDT P12_50

**Symbol:** NOT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1059 |
| net_profit_factor | 0.5729 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.9002 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -6.0467 |
| sortino_ratio | -2.8193 |
| max_drawdown | 0.9647 |
| cagr | -0.7416 |
| net_avg_win | 26.1435 |
| net_avg_loss | -39.8972 |
| avg_hold_time_bars | 7.1029 |
| exposure | 0.3533 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — GTC/USDT P8_26

**Symbol:** GTC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 741 |
| net_profit_factor | 0.6749 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9147 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -3.4958 |
| sortino_ratio | -1.3590 |
| max_drawdown | 0.7930 |
| cagr | -0.4637 |
| net_avg_win | 46.5122 |
| net_avg_loss | -62.7001 |
| avg_hold_time_bars | 7.1377 |
| exposure | 0.2404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

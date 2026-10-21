# EMA Hourly Continuation — FIL/USDT P12_34

**Symbol:** FIL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.7112 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 0.9593 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -2.4519 |
| sortino_ratio | -0.8133 |
| max_drawdown | 0.6162 |
| cagr | -0.3108 |
| net_avg_win | 56.8747 |
| net_avg_loss | -77.0378 |
| avg_hold_time_bars | 8.1063 |
| exposure | 0.1975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

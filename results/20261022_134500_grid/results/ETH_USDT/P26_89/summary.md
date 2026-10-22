# EMA Hourly Continuation — ETH/USDT P26_89

**Symbol:** ETH/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.4468 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.9437 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -6.8131 |
| sortino_ratio | -2.3797 |
| max_drawdown | 0.9536 |
| cagr | -0.7029 |
| net_avg_win | 28.8116 |
| net_avg_loss | -49.1945 |
| avg_hold_time_bars | 12.1702 |
| exposure | 0.3413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

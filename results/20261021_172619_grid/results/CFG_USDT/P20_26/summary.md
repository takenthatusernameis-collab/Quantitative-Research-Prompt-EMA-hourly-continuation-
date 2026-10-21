# EMA Hourly Continuation — CFG/USDT P20_26

**Symbol:** CFG/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 169 |
| net_profit_factor | 0.6179 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.8256 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -1.8651 |
| sortino_ratio | -0.3453 |
| max_drawdown | 0.3518 |
| cagr | -0.1462 |
| net_avg_win | 68.7909 |
| net_avg_loss | -93.1826 |
| avg_hold_time_bars | 31.9645 |
| exposure | 0.2455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

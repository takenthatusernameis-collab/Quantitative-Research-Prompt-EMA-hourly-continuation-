# EMA Hourly Continuation — AEVO/USDT P12_55

**Symbol:** AEVO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 996 |
| net_profit_factor | 0.6302 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.9901 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -5.1247 |
| sortino_ratio | -2.2661 |
| max_drawdown | 0.9389 |
| cagr | -0.6627 |
| net_avg_win | 33.9925 |
| net_avg_loss | -48.0031 |
| avg_hold_time_bars | 8.4659 |
| exposure | 0.3816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

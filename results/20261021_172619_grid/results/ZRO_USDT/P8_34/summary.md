# EMA Hourly Continuation — ZRO/USDT P8_34

**Symbol:** ZRO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.9318 |
| net_win_rate | 0.5357 |
| gross_profit_factor | 1.1473 |
| gross_win_rate | 0.5357 |
| sharpe_ratio | -0.5361 |
| sortino_ratio | -0.1975 |
| max_drawdown | 0.3305 |
| cagr | -0.0945 |
| net_avg_win | 87.4003 |
| net_avg_loss | -108.2031 |
| avg_hold_time_bars | 9.7861 |
| exposure | 0.2888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — LDO/USDT P12_26

**Symbol:** LDO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.7065 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9383 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -2.2041 |
| sortino_ratio | -0.6861 |
| max_drawdown | 0.5626 |
| cagr | -0.2697 |
| net_avg_win | 56.6381 |
| net_avg_loss | -77.4946 |
| avg_hold_time_bars | 5.0466 |
| exposure | 0.1083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

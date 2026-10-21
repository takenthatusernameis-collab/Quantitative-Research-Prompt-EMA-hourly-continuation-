# EMA Hourly Continuation — RLC/USDT P12_89

**Symbol:** RLC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.9380 |
| net_win_rate | 0.5417 |
| gross_profit_factor | 1.1728 |
| gross_win_rate | 0.5417 |
| sharpe_ratio | -0.3684 |
| sortino_ratio | -0.1107 |
| max_drawdown | 0.2729 |
| cagr | -0.0555 |
| net_avg_win | 86.4447 |
| net_avg_loss | -108.9129 |
| avg_hold_time_bars | 31.3773 |
| exposure | 0.6161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

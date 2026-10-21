# EMA Hourly Continuation — COTI/USDT P55_89

**Symbol:** COTI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.8601 |
| net_win_rate | 0.5374 |
| gross_profit_factor | 1.1485 |
| gross_win_rate | 0.5374 |
| sharpe_ratio | -0.7372 |
| sortino_ratio | -0.1829 |
| max_drawdown | 0.2048 |
| cagr | -0.0822 |
| net_avg_win | 75.3836 |
| net_avg_loss | -101.8253 |
| avg_hold_time_bars | 6.1088 |
| exposure | 0.0816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

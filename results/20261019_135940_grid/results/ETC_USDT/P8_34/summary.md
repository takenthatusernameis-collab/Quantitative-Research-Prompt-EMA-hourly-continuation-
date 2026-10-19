# EMA Hourly Continuation — ETC/USDT P8_34

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1402 |
| net_profit_factor | 0.3910 |
| net_win_rate | 0.4258 |
| gross_profit_factor | 0.8364 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -10.9670 |
| sortino_ratio | -5.7967 |
| max_drawdown | 0.9993 |
| cagr | -0.9455 |
| net_avg_win | 10.7475 |
| net_avg_loss | -20.3845 |
| avg_hold_time_bars | 5.3224 |
| exposure | 0.3392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

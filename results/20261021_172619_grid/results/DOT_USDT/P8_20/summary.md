# EMA Hourly Continuation — DOT/USDT P8_20

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.7686 |
| net_win_rate | 0.5248 |
| gross_profit_factor | 1.0967 |
| gross_win_rate | 0.5248 |
| sharpe_ratio | -1.6788 |
| sortino_ratio | -0.5110 |
| max_drawdown | 0.4850 |
| cagr | -0.2081 |
| net_avg_win | 63.2285 |
| net_avg_loss | -90.8394 |
| avg_hold_time_bars | 5.8333 |
| exposure | 0.1177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

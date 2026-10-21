# EMA Hourly Continuation — CHR/USDT P20_55

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.7159 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9213 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -2.6476 |
| sortino_ratio | -0.9047 |
| max_drawdown | 0.6592 |
| cagr | -0.3396 |
| net_avg_win | 59.6712 |
| net_avg_loss | -75.6264 |
| avg_hold_time_bars | 8.5069 |
| exposure | 0.2217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

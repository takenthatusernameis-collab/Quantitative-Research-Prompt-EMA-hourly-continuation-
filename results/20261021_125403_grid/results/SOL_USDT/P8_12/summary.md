# EMA Hourly Continuation — SOL/USDT P8_12

**Symbol:** SOL/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 213 |
| net_profit_factor | 0.9263 |
| net_win_rate | 0.5822 |
| gross_profit_factor | 1.3763 |
| gross_win_rate | 0.5822 |
| sharpe_ratio | -0.2919 |
| sortino_ratio | -0.0625 |
| max_drawdown | 0.1374 |
| cagr | -0.0304 |
| net_avg_win | 75.5739 |
| net_avg_loss | -113.6755 |
| avg_hold_time_bars | 4.8404 |
| exposure | 0.0469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

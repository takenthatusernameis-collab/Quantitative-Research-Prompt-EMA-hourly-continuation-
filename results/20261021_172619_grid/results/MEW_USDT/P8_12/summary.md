# EMA Hourly Continuation — MEW/USDT P8_12

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.6740 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9431 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -2.3755 |
| sortino_ratio | -0.5879 |
| max_drawdown | 0.5224 |
| cagr | -0.2370 |
| net_avg_win | 71.2899 |
| net_avg_loss | -96.9544 |
| avg_hold_time_bars | 4.4515 |
| exposure | 0.0605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

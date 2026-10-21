# EMA Hourly Continuation — SLP/USDT P50_55

**Symbol:** SLP/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 161 |
| net_profit_factor | 0.6523 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9673 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -1.9109 |
| sortino_ratio | -0.3481 |
| max_drawdown | 0.4224 |
| cagr | -0.1479 |
| net_avg_win | 80.6503 |
| net_avg_loss | -113.3398 |
| avg_hold_time_bars | 3.8882 |
| exposure | 0.0285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

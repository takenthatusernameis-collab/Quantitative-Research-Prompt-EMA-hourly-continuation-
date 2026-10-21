# EMA Hourly Continuation — CHR/USDT P8_100

**Symbol:** CHR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.8761 |
| net_win_rate | 0.5107 |
| gross_profit_factor | 1.0455 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -0.9135 |
| sortino_ratio | -0.2823 |
| max_drawdown | 0.3737 |
| cagr | -0.1253 |
| net_avg_win | 85.2139 |
| net_avg_loss | -101.5254 |
| avg_hold_time_bars | 32.7725 |
| exposure | 0.6911 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

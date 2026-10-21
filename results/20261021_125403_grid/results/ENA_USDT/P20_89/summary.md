# EMA Hourly Continuation — ENA/USDT P20_89

**Symbol:** ENA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.9644 |
| net_win_rate | 0.5316 |
| gross_profit_factor | 1.1261 |
| gross_win_rate | 0.5338 |
| sharpe_ratio | -0.1782 |
| sortino_ratio | -0.0560 |
| max_drawdown | 0.2817 |
| cagr | -0.0332 |
| net_avg_win | 87.5037 |
| net_avg_loss | -102.9910 |
| avg_hold_time_bars | 16.7975 |
| exposure | 0.3619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — MEW/USDT P34_100

**Symbol:** MEW/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.6512 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.8021 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -2.7449 |
| sortino_ratio | -0.8128 |
| max_drawdown | 0.6171 |
| cagr | -0.3113 |
| net_avg_win | 57.9090 |
| net_avg_loss | -72.6281 |
| avg_hold_time_bars | 12.1812 |
| exposure | 0.2414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

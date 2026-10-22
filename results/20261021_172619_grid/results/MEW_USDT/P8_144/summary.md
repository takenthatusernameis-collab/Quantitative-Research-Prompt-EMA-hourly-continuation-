# EMA Hourly Continuation — MEW/USDT P8_144

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.8691 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 0.9932 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -0.7453 |
| sortino_ratio | -0.1929 |
| max_drawdown | 0.2587 |
| cagr | -0.0878 |
| net_avg_win | 82.8857 |
| net_avg_loss | -96.5435 |
| avg_hold_time_bars | 50.5000 |
| exposure | 0.7529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

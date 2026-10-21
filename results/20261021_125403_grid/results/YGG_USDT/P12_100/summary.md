# EMA Hourly Continuation — YGG/USDT P12_100

**Symbol:** YGG/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.8484 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 1.0216 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -1.3114 |
| sortino_ratio | -0.4202 |
| max_drawdown | 0.4923 |
| cagr | -0.1778 |
| net_avg_win | 86.5492 |
| net_avg_loss | -102.4244 |
| avg_hold_time_bars | 24.9722 |
| exposure | 0.5684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

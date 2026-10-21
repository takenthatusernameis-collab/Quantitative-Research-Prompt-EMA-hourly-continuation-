# EMA Hourly Continuation — SNX/USDT P50_89

**Symbol:** SNX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.8909 |
| net_win_rate | 0.5429 |
| gross_profit_factor | 1.1870 |
| gross_win_rate | 0.5429 |
| sharpe_ratio | -0.6753 |
| sortino_ratio | -0.1856 |
| max_drawdown | 0.2736 |
| cagr | -0.0843 |
| net_avg_win | 82.9398 |
| net_avg_loss | -110.5920 |
| avg_hold_time_bars | 7.5235 |
| exposure | 0.1229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — JST/USDT P50_100

**Symbol:** JST/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.6077 |
| net_win_rate | 0.5346 |
| gross_profit_factor | 1.1368 |
| gross_win_rate | 0.5402 |
| sharpe_ratio | -2.5961 |
| sortino_ratio | -0.7066 |
| max_drawdown | 0.5680 |
| cagr | -0.2789 |
| net_avg_win | 45.0779 |
| net_avg_loss | -85.2199 |
| avg_hold_time_bars | 10.2022 |
| exposure | 0.1667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

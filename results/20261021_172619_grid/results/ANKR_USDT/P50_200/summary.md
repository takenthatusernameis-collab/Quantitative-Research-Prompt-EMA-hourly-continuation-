# EMA Hourly Continuation — ANKR/USDT P50_200

**Symbol:** ANKR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.8388 |
| net_win_rate | 0.5196 |
| gross_profit_factor | 1.0888 |
| gross_win_rate | 0.5196 |
| sharpe_ratio | -0.9920 |
| sortino_ratio | -0.2494 |
| max_drawdown | 0.2983 |
| cagr | -0.1097 |
| net_avg_win | 82.8196 |
| net_avg_loss | -106.7934 |
| avg_hold_time_bars | 32.3922 |
| exposure | 0.4505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

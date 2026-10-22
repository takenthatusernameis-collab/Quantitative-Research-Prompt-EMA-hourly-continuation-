# EMA Hourly Continuation — SWFTC/USDT P26_200

**Symbol:** SWFTC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.7428 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.9016 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -1.7426 |
| sortino_ratio | -0.4394 |
| max_drawdown | 0.4082 |
| cagr | -0.1836 |
| net_avg_win | 77.3852 |
| net_avg_loss | -93.5088 |
| avg_hold_time_bars | 34.7175 |
| exposure | 0.4971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

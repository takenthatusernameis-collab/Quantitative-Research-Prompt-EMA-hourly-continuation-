# EMA Hourly Continuation — MOCA/USDT P55_200

**Symbol:** MOCA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.8753 |
| net_win_rate | 0.5223 |
| gross_profit_factor | 1.0760 |
| gross_win_rate | 0.5223 |
| sharpe_ratio | -0.6343 |
| sortino_ratio | -0.1506 |
| max_drawdown | 0.2663 |
| cagr | -0.0692 |
| net_avg_win | 82.0126 |
| net_avg_loss | -102.4257 |
| avg_hold_time_bars | 30.4170 |
| exposure | 0.3766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

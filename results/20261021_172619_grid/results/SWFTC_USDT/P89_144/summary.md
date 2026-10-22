# EMA Hourly Continuation — SWFTC/USDT P89_144

**Symbol:** SWFTC/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 237 |
| net_profit_factor | 0.7011 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.9064 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -1.7935 |
| sortino_ratio | -0.3938 |
| max_drawdown | 0.3956 |
| cagr | -0.1650 |
| net_avg_win | 76.2569 |
| net_avg_loss | -97.4578 |
| avg_hold_time_bars | 8.0675 |
| exposure | 0.0869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

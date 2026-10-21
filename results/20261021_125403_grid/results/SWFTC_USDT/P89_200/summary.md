# EMA Hourly Continuation — SWFTC/USDT P89_200

**Symbol:** SWFTC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.7201 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -1.7612 |
| sortino_ratio | -0.4011 |
| max_drawdown | 0.3917 |
| cagr | -0.1684 |
| net_avg_win | 79.4807 |
| net_avg_loss | -97.3835 |
| avg_hold_time_bars | 15.8203 |
| exposure | 0.1841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

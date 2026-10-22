# EMA Hourly Continuation — SWFTC/USDT P50_144

**Symbol:** SWFTC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.7308 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9146 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -1.8326 |
| sortino_ratio | -0.4627 |
| max_drawdown | 0.4291 |
| cagr | -0.1921 |
| net_avg_win | 75.5756 |
| net_avg_loss | -93.3880 |
| avg_hold_time_bars | 15.5732 |
| exposure | 0.2223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

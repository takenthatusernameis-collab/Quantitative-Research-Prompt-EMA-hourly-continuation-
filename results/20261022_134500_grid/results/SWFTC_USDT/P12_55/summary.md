# EMA Hourly Continuation — SWFTC/USDT P12_55

**Symbol:** SWFTC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1031 |
| net_profit_factor | 0.4402 |
| net_win_rate | 0.4083 |
| gross_profit_factor | 0.7410 |
| gross_win_rate | 0.4210 |
| sharpe_ratio | -8.6183 |
| sortino_ratio | -3.8661 |
| max_drawdown | 0.9924 |
| cagr | -0.8567 |
| net_avg_win | 18.5343 |
| net_avg_loss | -29.0604 |
| avg_hold_time_bars | 7.2415 |
| exposure | 0.3394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

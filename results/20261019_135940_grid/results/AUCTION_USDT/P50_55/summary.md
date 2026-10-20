# EMA Hourly Continuation — AUCTION/USDT P50_55

**Symbol:** AUCTION/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 813 |
| net_profit_factor | 0.2707 |
| net_win_rate | 0.3358 |
| gross_profit_factor | 0.8064 |
| gross_win_rate | 0.4170 |
| sharpe_ratio | -12.3079 |
| sortino_ratio | -5.1333 |
| max_drawdown | 0.9990 |
| cagr | -0.9360 |
| net_avg_win | 13.5852 |
| net_avg_loss | -25.3686 |
| avg_hold_time_bars | 2.8278 |
| exposure | 0.1041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

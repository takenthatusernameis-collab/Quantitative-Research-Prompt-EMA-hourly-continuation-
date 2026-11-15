# EMA Hourly Continuation — CERE/USDT P12_34

**Symbol:** CERE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1278 |
| net_profit_factor | 0.3373 |
| net_win_rate | 0.3114 |
| gross_profit_factor | 0.6945 |
| gross_win_rate | 0.3764 |
| sharpe_ratio | -15.5614 |
| sortino_ratio | -7.9973 |
| max_drawdown | 1.0000 |
| cagr | -0.9860 |
| net_avg_win | 12.7872 |
| net_avg_loss | -17.1467 |
| avg_hold_time_bars | 4.9186 |
| exposure | 0.2857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

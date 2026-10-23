# EMA Hourly Continuation — HNT/USDT P21_34

**Symbol:** HNT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1165 |
| net_profit_factor | 0.3628 |
| net_win_rate | 0.3906 |
| gross_profit_factor | 0.7380 |
| gross_win_rate | 0.4112 |
| sharpe_ratio | -11.2551 |
| sortino_ratio | -5.4401 |
| max_drawdown | 0.9990 |
| cagr | -0.9364 |
| net_avg_win | 12.5028 |
| net_avg_loss | -22.0829 |
| avg_hold_time_bars | 2.5931 |
| exposure | 0.1373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

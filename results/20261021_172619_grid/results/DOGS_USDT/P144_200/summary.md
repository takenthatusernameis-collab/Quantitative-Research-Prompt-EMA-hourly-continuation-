# EMA Hourly Continuation — DOGS/USDT P144_200

**Symbol:** DOGS/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 158 |
| net_profit_factor | 0.9041 |
| net_win_rate | 0.5380 |
| gross_profit_factor | 1.1577 |
| gross_win_rate | 0.5380 |
| sharpe_ratio | -0.3781 |
| sortino_ratio | -0.0744 |
| max_drawdown | 0.1098 |
| cagr | -0.0355 |
| net_avg_win | 83.0479 |
| net_avg_loss | -106.9540 |
| avg_hold_time_bars | 7.4177 |
| exposure | 0.0622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

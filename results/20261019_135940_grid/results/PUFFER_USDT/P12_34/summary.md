# EMA Hourly Continuation — PUFFER/USDT P12_34

**Symbol:** PUFFER/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 927 |
| net_profit_factor | 0.5551 |
| net_win_rate | 0.4736 |
| gross_profit_factor | 0.8924 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -6.0155 |
| sortino_ratio | -2.8788 |
| max_drawdown | 0.9397 |
| cagr | -0.7489 |
| net_avg_win | 26.6702 |
| net_avg_loss | -43.2219 |
| avg_hold_time_bars | 4.9331 |
| exposure | 0.2588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

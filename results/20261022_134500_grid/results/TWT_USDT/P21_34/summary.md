# EMA Hourly Continuation — TWT/USDT P21_34

**Symbol:** TWT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1224 |
| net_profit_factor | 0.2752 |
| net_win_rate | 0.4060 |
| gross_profit_factor | 0.7890 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -12.5817 |
| sortino_ratio | -6.3073 |
| max_drawdown | 0.9998 |
| cagr | -0.9628 |
| net_avg_win | 7.6377 |
| net_avg_loss | -18.9730 |
| avg_hold_time_bars | 2.6315 |
| exposure | 0.1464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

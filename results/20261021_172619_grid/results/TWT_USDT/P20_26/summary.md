# EMA Hourly Continuation — TWT/USDT P20_26

**Symbol:** TWT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.5492 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.8974 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -2.6861 |
| sortino_ratio | -0.6046 |
| max_drawdown | 0.5129 |
| cagr | -0.2411 |
| net_avg_win | 52.0564 |
| net_avg_loss | -87.3149 |
| avg_hold_time_bars | 4.6762 |
| exposure | 0.0519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

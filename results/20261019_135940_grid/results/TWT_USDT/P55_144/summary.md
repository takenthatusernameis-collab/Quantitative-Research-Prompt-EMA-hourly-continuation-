# EMA Hourly Continuation — TWT/USDT P55_144

**Symbol:** TWT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.4714 |
| net_win_rate | 0.4471 |
| gross_profit_factor | 0.8578 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -5.2131 |
| sortino_ratio | -1.6577 |
| max_drawdown | 0.8772 |
| cagr | -0.5547 |
| net_avg_win | 33.9839 |
| net_avg_loss | -58.2882 |
| avg_hold_time_bars | 11.2824 |
| exposure | 0.2615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

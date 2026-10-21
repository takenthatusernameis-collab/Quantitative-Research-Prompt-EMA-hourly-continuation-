# EMA Hourly Continuation — AR/USDT P55_89

**Symbol:** AR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.6820 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.8997 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.0812 |
| sortino_ratio | -0.5508 |
| max_drawdown | 0.4748 |
| cagr | -0.2234 |
| net_avg_win | 61.0918 |
| net_avg_loss | -83.0330 |
| avg_hold_time_bars | 5.7493 |
| exposure | 0.0896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

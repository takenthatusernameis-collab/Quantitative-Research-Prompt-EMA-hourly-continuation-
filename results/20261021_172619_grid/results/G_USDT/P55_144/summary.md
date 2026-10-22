# EMA Hourly Continuation — G/USDT P55_144

**Symbol:** G/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.7097 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9354 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -1.8462 |
| sortino_ratio | -0.4792 |
| max_drawdown | 0.4271 |
| cagr | -0.1971 |
| net_avg_win | 66.6608 |
| net_avg_loss | -89.4277 |
| avg_hold_time_bars | 16.9018 |
| exposure | 0.2533 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

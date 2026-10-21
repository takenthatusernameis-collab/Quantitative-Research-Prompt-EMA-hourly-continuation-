# EMA Hourly Continuation — APE/USDT P21_144

**Symbol:** APE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.8185 |
| net_win_rate | 0.4986 |
| gross_profit_factor | 0.9814 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -1.1325 |
| sortino_ratio | -0.3114 |
| max_drawdown | 0.3407 |
| cagr | -0.1352 |
| net_avg_win | 74.8910 |
| net_avg_loss | -91.0074 |
| avg_hold_time_bars | 30.8049 |
| exposure | 0.5167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

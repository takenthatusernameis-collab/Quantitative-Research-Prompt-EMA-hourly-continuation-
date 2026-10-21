# EMA Hourly Continuation — BAT/USDT P55_200

**Symbol:** BAT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.8053 |
| net_win_rate | 0.5096 |
| gross_profit_factor | 1.0256 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -1.1277 |
| sortino_ratio | -0.2867 |
| max_drawdown | 0.3401 |
| cagr | -0.1244 |
| net_avg_win | 73.3010 |
| net_avg_loss | -94.5727 |
| avg_hold_time_bars | 23.5796 |
| exposure | 0.3365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

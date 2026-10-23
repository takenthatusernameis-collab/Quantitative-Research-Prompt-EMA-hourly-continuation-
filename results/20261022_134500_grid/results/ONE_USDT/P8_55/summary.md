# EMA Hourly Continuation — ONE/USDT P8_55

**Symbol:** ONE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 961 |
| net_profit_factor | 0.5391 |
| net_win_rate | 0.4370 |
| gross_profit_factor | 0.8170 |
| gross_win_rate | 0.4443 |
| sharpe_ratio | -6.5119 |
| sortino_ratio | -2.8277 |
| max_drawdown | 0.9707 |
| cagr | -0.7470 |
| net_avg_win | 26.9645 |
| net_avg_loss | -38.8319 |
| avg_hold_time_bars | 12.1779 |
| exposure | 0.5320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

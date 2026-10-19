# EMA Hourly Continuation — KCS/USDT P55_89

**Symbol:** KCS/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.1641 |
| net_win_rate | 0.3504 |
| gross_profit_factor | 0.6516 |
| gross_win_rate | 0.4170 |
| sharpe_ratio | -11.7785 |
| sortino_ratio | -4.6346 |
| max_drawdown | 0.9981 |
| cagr | -0.9162 |
| net_avg_win | 7.9342 |
| net_avg_loss | -26.0699 |
| avg_hold_time_bars | 4.2681 |
| exposure | 0.1368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

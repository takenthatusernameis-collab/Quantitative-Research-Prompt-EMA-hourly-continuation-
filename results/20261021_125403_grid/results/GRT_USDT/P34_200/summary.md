# EMA Hourly Continuation — GRT/USDT P34_200

**Symbol:** GRT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.8853 |
| net_win_rate | 0.5180 |
| gross_profit_factor | 1.0549 |
| gross_win_rate | 0.5180 |
| sharpe_ratio | -0.5815 |
| sortino_ratio | -0.1388 |
| max_drawdown | 0.2262 |
| cagr | -0.0645 |
| net_avg_win | 83.0184 |
| net_avg_loss | -100.7750 |
| avg_hold_time_bars | 40.0576 |
| exposure | 0.5039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

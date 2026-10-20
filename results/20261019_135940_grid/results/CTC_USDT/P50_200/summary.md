# EMA Hourly Continuation — CTC/USDT P50_200

**Symbol:** CTC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.5906 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.9490 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -3.4737 |
| sortino_ratio | -1.0086 |
| max_drawdown | 0.7274 |
| cagr | -0.3892 |
| net_avg_win | 50.9560 |
| net_avg_loss | -75.7308 |
| avg_hold_time_bars | 17.9837 |
| exposure | 0.3515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

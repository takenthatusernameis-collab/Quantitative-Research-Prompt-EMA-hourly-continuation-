# EMA Hourly Continuation — HTX/USDT P8_34

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.4580 |
| net_win_rate | 0.3796 |
| gross_profit_factor | 0.7778 |
| gross_win_rate | 0.3867 |
| sharpe_ratio | -8.5401 |
| sortino_ratio | -3.2774 |
| max_drawdown | 0.9806 |
| cagr | -0.7899 |
| net_avg_win | 30.9152 |
| net_avg_loss | -41.3013 |
| avg_hold_time_bars | 10.0297 |
| exposure | 0.3204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

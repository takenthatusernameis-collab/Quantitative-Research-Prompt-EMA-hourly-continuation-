# EMA Hourly Continuation — SNX/USDT P21_50

**Symbol:** SNX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1004 |
| net_profit_factor | 0.5743 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 1.0580 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -5.8984 |
| sortino_ratio | -2.6231 |
| max_drawdown | 0.9610 |
| cagr | -0.7202 |
| net_avg_win | 26.3703 |
| net_avg_loss | -43.9486 |
| avg_hold_time_bars | 4.3586 |
| exposure | 0.1980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

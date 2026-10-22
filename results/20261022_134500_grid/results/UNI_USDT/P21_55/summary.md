# EMA Hourly Continuation — UNI/USDT P21_55

**Symbol:** UNI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 985 |
| net_profit_factor | 0.4906 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.8971 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -7.1400 |
| sortino_ratio | -3.1422 |
| max_drawdown | 0.9807 |
| cagr | -0.7903 |
| net_avg_win | 21.0221 |
| net_avg_loss | -35.8973 |
| avg_hold_time_bars | 4.7766 |
| exposure | 0.2139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

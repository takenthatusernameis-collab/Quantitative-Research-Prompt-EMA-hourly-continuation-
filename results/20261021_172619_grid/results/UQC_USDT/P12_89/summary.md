# EMA Hourly Continuation — UQC/USDT P12_89

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.3411 |
| net_win_rate | 0.2620 |
| gross_profit_factor | 0.5133 |
| gross_win_rate | 0.2989 |
| sharpe_ratio | -7.2271 |
| sortino_ratio | -1.6760 |
| max_drawdown | 0.9078 |
| cagr | -0.6114 |
| net_avg_win | 66.1909 |
| net_avg_loss | -68.8877 |
| avg_hold_time_bars | 50.2694 |
| exposure | 0.6166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

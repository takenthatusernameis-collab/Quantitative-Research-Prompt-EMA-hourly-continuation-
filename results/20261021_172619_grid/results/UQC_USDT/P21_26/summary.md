# EMA Hourly Continuation — UQC/USDT P21_26

**Symbol:** UQC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 195 |
| net_profit_factor | 0.2957 |
| net_win_rate | 0.2821 |
| gross_profit_factor | 0.4930 |
| gross_win_rate | 0.3077 |
| sharpe_ratio | -5.3745 |
| sortino_ratio | -1.0686 |
| max_drawdown | 0.7243 |
| cagr | -0.3997 |
| net_avg_win | 55.2535 |
| net_avg_loss | -73.4166 |
| avg_hold_time_bars | 47.4667 |
| exposure | 0.4189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

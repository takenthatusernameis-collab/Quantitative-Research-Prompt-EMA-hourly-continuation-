# EMA Hourly Continuation — ALT/USDT P21_55

**Symbol:** ALT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 826 |
| net_profit_factor | 0.5469 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.8622 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -5.8142 |
| sortino_ratio | -2.3535 |
| max_drawdown | 0.9442 |
| cagr | -0.6746 |
| net_avg_win | 31.2739 |
| net_avg_loss | -44.8299 |
| avg_hold_time_bars | 6.5133 |
| exposure | 0.2445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

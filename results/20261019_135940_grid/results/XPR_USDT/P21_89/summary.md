# EMA Hourly Continuation — XPR/USDT P21_89

**Symbol:** XPR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.4323 |
| net_win_rate | 0.4242 |
| gross_profit_factor | 0.7912 |
| gross_win_rate | 0.4284 |
| sharpe_ratio | -7.1819 |
| sortino_ratio | -2.6645 |
| max_drawdown | 0.9699 |
| cagr | -0.7474 |
| net_avg_win | 24.4175 |
| net_avg_loss | -41.6055 |
| avg_hold_time_bars | 10.1784 |
| exposure | 0.3294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

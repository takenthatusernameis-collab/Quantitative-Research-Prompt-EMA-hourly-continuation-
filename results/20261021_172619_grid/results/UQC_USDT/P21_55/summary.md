# EMA Hourly Continuation — UQC/USDT P21_55

**Symbol:** UQC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.3693 |
| net_win_rate | 0.3144 |
| gross_profit_factor | 0.5661 |
| gross_win_rate | 0.3258 |
| sharpe_ratio | -5.3953 |
| sortino_ratio | -1.2280 |
| max_drawdown | 0.7772 |
| cagr | -0.4464 |
| net_avg_win | 54.6714 |
| net_avg_loss | -67.8848 |
| avg_hold_time_bars | 44.0227 |
| exposure | 0.5260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

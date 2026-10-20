# EMA Hourly Continuation — GMT/USDT P21_100

**Symbol:** GMT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.5917 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.9210 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -5.0628 |
| sortino_ratio | -1.8631 |
| max_drawdown | 0.9052 |
| cagr | -0.5925 |
| net_avg_win | 42.2446 |
| net_avg_loss | -58.2978 |
| avg_hold_time_bars | 13.4802 |
| exposure | 0.4185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

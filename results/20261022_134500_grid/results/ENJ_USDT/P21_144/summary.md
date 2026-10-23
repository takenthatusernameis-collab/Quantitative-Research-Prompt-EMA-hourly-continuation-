# EMA Hourly Continuation — ENJ/USDT P21_144

**Symbol:** ENJ/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.7381 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 1.0709 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -2.2512 |
| sortino_ratio | -0.6958 |
| max_drawdown | 0.6208 |
| cagr | -0.2823 |
| net_avg_win | 66.8437 |
| net_avg_loss | -88.7073 |
| avg_hold_time_bars | 25.7039 |
| exposure | 0.5618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

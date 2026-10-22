# EMA Hourly Continuation — XTZ/USDT P21_144

**Symbol:** XTZ/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.6782 |
| net_win_rate | 0.4876 |
| gross_profit_factor | 1.0314 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -2.5529 |
| sortino_ratio | -0.7598 |
| max_drawdown | 0.6122 |
| cagr | -0.3008 |
| net_avg_win | 57.8522 |
| net_avg_loss | -81.1689 |
| avg_hold_time_bars | 29.6208 |
| exposure | 0.5965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

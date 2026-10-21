# EMA Hourly Continuation — ENJ/USDT P21_55

**Symbol:** ENJ/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.7205 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9670 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -2.5174 |
| sortino_ratio | -0.8235 |
| max_drawdown | 0.6492 |
| cagr | -0.3149 |
| net_avg_win | 61.9214 |
| net_avg_loss | -81.4836 |
| avg_hold_time_bars | 8.0019 |
| exposure | 0.1905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

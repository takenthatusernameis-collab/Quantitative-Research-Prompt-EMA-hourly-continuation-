# EMA Hourly Continuation — AXS/USDT P26_89

**Symbol:** AXS/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.9121 |
| net_win_rate | 0.5445 |
| gross_profit_factor | 1.1852 |
| gross_win_rate | 0.5445 |
| sharpe_ratio | -0.5962 |
| sortino_ratio | -0.1848 |
| max_drawdown | 0.2801 |
| cagr | -0.0859 |
| net_avg_win | 83.8459 |
| net_avg_loss | -109.8713 |
| avg_hold_time_bars | 13.0239 |
| exposure | 0.2717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

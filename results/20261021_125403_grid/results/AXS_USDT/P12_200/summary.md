# EMA Hourly Continuation — AXS/USDT P12_200

**Symbol:** AXS/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.8896 |
| net_win_rate | 0.5175 |
| gross_profit_factor | 1.0623 |
| gross_win_rate | 0.5175 |
| sharpe_ratio | -0.5973 |
| sortino_ratio | -0.1447 |
| max_drawdown | 0.2433 |
| cagr | -0.0669 |
| net_avg_win | 87.1840 |
| net_avg_loss | -105.1094 |
| avg_hold_time_bars | 55.1853 |
| exposure | 0.7142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

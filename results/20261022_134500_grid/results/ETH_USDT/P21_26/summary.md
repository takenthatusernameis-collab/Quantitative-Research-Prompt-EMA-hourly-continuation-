# EMA Hourly Continuation — ETH/USDT P21_26

**Symbol:** ETH/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1136 |
| net_profit_factor | 0.1051 |
| net_win_rate | 0.2597 |
| gross_profit_factor | 0.7001 |
| gross_win_rate | 0.3820 |
| sharpe_ratio | -18.9233 |
| sortino_ratio | -10.1076 |
| max_drawdown | 1.0000 |
| cagr | -0.9966 |
| net_avg_win | 3.9818 |
| net_avg_loss | -13.2873 |
| avg_hold_time_bars | 1.8838 |
| exposure | 0.0973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

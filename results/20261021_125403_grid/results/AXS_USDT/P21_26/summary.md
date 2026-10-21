# EMA Hourly Continuation — AXS/USDT P21_26

**Symbol:** AXS/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 151 |
| net_profit_factor | 0.6480 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9637 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -1.6713 |
| sortino_ratio | -0.2945 |
| max_drawdown | 0.3186 |
| cagr | -0.1263 |
| net_avg_win | 71.7876 |
| net_avg_loss | -106.4714 |
| avg_hold_time_bars | 4.6954 |
| exposure | 0.0321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

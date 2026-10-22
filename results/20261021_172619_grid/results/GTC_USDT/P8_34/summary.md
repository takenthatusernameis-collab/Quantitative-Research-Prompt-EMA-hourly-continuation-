# EMA Hourly Continuation — GTC/USDT P8_34

**Symbol:** GTC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 769 |
| net_profit_factor | 0.6878 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.9025 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -3.5220 |
| sortino_ratio | -1.3916 |
| max_drawdown | 0.8034 |
| cagr | -0.4729 |
| net_avg_win | 48.8082 |
| net_avg_loss | -62.7865 |
| avg_hold_time_bars | 8.8752 |
| exposure | 0.3102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

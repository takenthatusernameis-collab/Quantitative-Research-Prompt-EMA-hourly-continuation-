# EMA Hourly Continuation — JUP/USDT P21_50

**Symbol:** JUP/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 969 |
| net_profit_factor | 0.5526 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9207 |
| gross_win_rate | 0.4809 |
| sharpe_ratio | -5.7759 |
| sortino_ratio | -2.5417 |
| max_drawdown | 0.9535 |
| cagr | -0.7026 |
| net_avg_win | 25.6807 |
| net_avg_loss | -41.6556 |
| avg_hold_time_bars | 4.6543 |
| exposure | 0.2050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

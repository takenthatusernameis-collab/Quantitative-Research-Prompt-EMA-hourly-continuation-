# EMA Hourly Continuation — APT/USDT P8_26

**Symbol:** APT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.7088 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9513 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -2.7446 |
| sortino_ratio | -0.9541 |
| max_drawdown | 0.6690 |
| cagr | -0.3536 |
| net_avg_win | 56.6541 |
| net_avg_loss | -75.1987 |
| avg_hold_time_bars | 7.1949 |
| exposure | 0.1930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

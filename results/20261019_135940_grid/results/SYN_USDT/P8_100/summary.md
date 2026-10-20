# EMA Hourly Continuation — SYN/USDT P8_100

**Symbol:** SYN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.7165 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9999 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -2.7921 |
| sortino_ratio | -0.9704 |
| max_drawdown | 0.6943 |
| cagr | -0.3742 |
| net_avg_win | 58.4935 |
| net_avg_loss | -77.7330 |
| avg_hold_time_bars | 24.7863 |
| exposure | 0.6906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

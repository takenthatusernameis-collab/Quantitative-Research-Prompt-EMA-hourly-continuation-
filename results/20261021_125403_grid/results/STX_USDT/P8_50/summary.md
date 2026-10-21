# EMA Hourly Continuation — STX/USDT P8_50

**Symbol:** STX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.7649 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9608 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -2.1878 |
| sortino_ratio | -0.8208 |
| max_drawdown | 0.6333 |
| cagr | -0.3144 |
| net_avg_win | 58.5798 |
| net_avg_loss | -74.6200 |
| avg_hold_time_bars | 14.3198 |
| exposure | 0.4478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

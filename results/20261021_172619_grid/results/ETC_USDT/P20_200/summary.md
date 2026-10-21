# EMA Hourly Continuation — ETC/USDT P20_200

**Symbol:** ETC/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.7687 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9766 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -1.4159 |
| sortino_ratio | -0.3485 |
| max_drawdown | 0.3930 |
| cagr | -0.1489 |
| net_avg_win | 75.2785 |
| net_avg_loss | -95.9724 |
| avg_hold_time_bars | 45.3300 |
| exposure | 0.6120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

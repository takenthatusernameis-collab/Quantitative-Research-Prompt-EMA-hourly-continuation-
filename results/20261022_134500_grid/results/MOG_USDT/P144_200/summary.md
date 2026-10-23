# EMA Hourly Continuation — MOG/USDT P144_200

**Symbol:** MOG/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.5847 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8576 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -3.5230 |
| sortino_ratio | -1.0022 |
| max_drawdown | 0.6796 |
| cagr | -0.3833 |
| net_avg_win | 55.1936 |
| net_avg_loss | -80.3088 |
| avg_hold_time_bars | 4.8414 |
| exposure | 0.0895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

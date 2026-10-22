# EMA Hourly Continuation — TRX/USDT P12_26

**Symbol:** TRX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1216 |
| net_profit_factor | 0.1204 |
| net_win_rate | 0.2738 |
| gross_profit_factor | 0.8880 |
| gross_win_rate | 0.4441 |
| sharpe_ratio | -18.9987 |
| sortino_ratio | -10.5573 |
| max_drawdown | 1.0000 |
| cagr | -0.9970 |
| net_avg_win | 4.1123 |
| net_avg_loss | -12.8759 |
| avg_hold_time_bars | 3.2286 |
| exposure | 0.1785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

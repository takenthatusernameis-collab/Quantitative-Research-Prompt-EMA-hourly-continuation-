# EMA Hourly Continuation — HTX/USDT P21_34

**Symbol:** HTX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1286 |
| net_profit_factor | 0.0749 |
| net_win_rate | 0.2061 |
| gross_profit_factor | 0.3603 |
| gross_win_rate | 0.3048 |
| sharpe_ratio | -21.5978 |
| sortino_ratio | -12.3112 |
| max_drawdown | 1.0000 |
| cagr | -0.9989 |
| net_avg_win | 3.0546 |
| net_avg_loss | -10.5871 |
| avg_hold_time_bars | 3.1369 |
| exposure | 0.1826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

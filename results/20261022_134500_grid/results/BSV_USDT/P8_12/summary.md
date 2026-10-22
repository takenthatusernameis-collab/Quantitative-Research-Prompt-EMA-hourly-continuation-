# EMA Hourly Continuation — BSV/USDT P8_12

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1938 |
| net_profit_factor | 0.1815 |
| net_win_rate | 0.3230 |
| gross_profit_factor | 0.7640 |
| gross_win_rate | 0.4071 |
| sharpe_ratio | -20.8763 |
| sortino_ratio | -13.5375 |
| max_drawdown | 1.0000 |
| cagr | -0.9993 |
| net_avg_win | 3.5420 |
| net_avg_loss | -9.3120 |
| avg_hold_time_bars | 1.9948 |
| exposure | 0.1757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

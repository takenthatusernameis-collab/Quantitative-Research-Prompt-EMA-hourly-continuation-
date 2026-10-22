# EMA Hourly Continuation — TRX/USDT P20_50

**Symbol:** TRX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 851 |
| net_profit_factor | 0.2142 |
| net_win_rate | 0.3537 |
| gross_profit_factor | 0.9049 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -13.2810 |
| sortino_ratio | -5.7728 |
| max_drawdown | 0.9997 |
| cagr | -0.9591 |
| net_avg_win | 9.0506 |
| net_avg_loss | -23.1290 |
| avg_hold_time_bars | 5.0928 |
| exposure | 0.1970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

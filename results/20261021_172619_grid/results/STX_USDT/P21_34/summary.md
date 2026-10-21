# EMA Hourly Continuation — STX/USDT P21_34

**Symbol:** STX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.7466 |
| net_win_rate | 0.5141 |
| gross_profit_factor | 1.0330 |
| gross_win_rate | 0.5141 |
| sharpe_ratio | -1.3986 |
| sortino_ratio | -0.3386 |
| max_drawdown | 0.3858 |
| cagr | -0.1431 |
| net_avg_win | 65.1355 |
| net_avg_loss | -92.2959 |
| avg_hold_time_bars | 5.7958 |
| exposure | 0.0745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

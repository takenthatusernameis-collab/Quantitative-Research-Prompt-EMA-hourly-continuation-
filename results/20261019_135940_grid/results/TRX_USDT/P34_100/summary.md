# EMA Hourly Continuation — TRX/USDT P34_100

**Symbol:** TRX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.2967 |
| net_win_rate | 0.3669 |
| gross_profit_factor | 1.0045 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -9.6500 |
| sortino_ratio | -3.4233 |
| max_drawdown | 0.9891 |
| cagr | -0.8343 |
| net_avg_win | 19.4032 |
| net_avg_loss | -37.9034 |
| avg_hold_time_bars | 9.2184 |
| exposure | 0.2455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

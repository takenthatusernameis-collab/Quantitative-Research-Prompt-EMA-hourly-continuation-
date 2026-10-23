# EMA Hourly Continuation — W/USDT P20_100

**Symbol:** W/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.7312 |
| net_win_rate | 0.5007 |
| gross_profit_factor | 1.0550 |
| gross_win_rate | 0.5081 |
| sharpe_ratio | -2.8486 |
| sortino_ratio | -1.0425 |
| max_drawdown | 0.7440 |
| cagr | -0.3932 |
| net_avg_win | 57.1762 |
| net_avg_loss | -78.4296 |
| avg_hold_time_bars | 13.6745 |
| exposure | 0.4220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

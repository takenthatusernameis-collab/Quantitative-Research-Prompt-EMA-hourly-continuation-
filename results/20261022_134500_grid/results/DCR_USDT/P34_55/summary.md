# EMA Hourly Continuation — DCR/USDT P34_55

**Symbol:** DCR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 901 |
| net_profit_factor | 0.3983 |
| net_win_rate | 0.4151 |
| gross_profit_factor | 0.8660 |
| gross_win_rate | 0.4428 |
| sharpe_ratio | -9.0266 |
| sortino_ratio | -3.8382 |
| max_drawdown | 0.9925 |
| cagr | -0.8542 |
| net_avg_win | 17.5637 |
| net_avg_loss | -31.2925 |
| avg_hold_time_bars | 3.5838 |
| exposure | 0.1461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

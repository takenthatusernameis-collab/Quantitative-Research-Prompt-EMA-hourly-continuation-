# EMA Hourly Continuation — KNC/USDT P89_100

**Symbol:** KNC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.3214 |
| net_win_rate | 0.4007 |
| gross_profit_factor | 0.9803 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -8.5962 |
| sortino_ratio | -2.9282 |
| max_drawdown | 0.9785 |
| cagr | -0.7825 |
| net_avg_win | 20.8705 |
| net_avg_loss | -43.4232 |
| avg_hold_time_bars | 3.2130 |
| exposure | 0.0809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — IOTX/USDT P21_55

**Symbol:** IOTX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 975 |
| net_profit_factor | 0.5750 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 1.0195 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -6.6364 |
| sortino_ratio | -2.9345 |
| max_drawdown | 0.9726 |
| cagr | -0.7566 |
| net_avg_win | 28.9449 |
| net_avg_loss | -43.8642 |
| avg_hold_time_bars | 4.9826 |
| exposure | 0.2208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

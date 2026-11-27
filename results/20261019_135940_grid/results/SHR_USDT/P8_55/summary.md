# EMA Hourly Continuation — SHR/USDT P8_55

**Symbol:** SHR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1422 |
| net_profit_factor | 0.4766 |
| net_win_rate | 0.3572 |
| gross_profit_factor | 0.6973 |
| gross_win_rate | 0.3594 |
| sharpe_ratio | -10.5870 |
| sortino_ratio | -5.5660 |
| max_drawdown | 0.9989 |
| cagr | -0.9316 |
| net_avg_win | 17.9057 |
| net_avg_loss | -20.8803 |
| avg_hold_time_bars | 6.6041 |
| exposure | 0.4250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

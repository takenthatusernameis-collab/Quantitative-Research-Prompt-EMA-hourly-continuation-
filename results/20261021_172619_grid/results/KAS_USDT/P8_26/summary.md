# EMA Hourly Continuation — KAS/USDT P8_26

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.8830 |
| net_win_rate | 0.5450 |
| gross_profit_factor | 1.1882 |
| gross_win_rate | 0.5450 |
| sharpe_ratio | -0.9228 |
| sortino_ratio | -0.3306 |
| max_drawdown | 0.3827 |
| cagr | -0.1447 |
| net_avg_win | 73.5622 |
| net_avg_loss | -99.7943 |
| avg_hold_time_bars | 6.9002 |
| exposure | 0.1916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

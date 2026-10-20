# EMA Hourly Continuation — RSR/USDT P8_12

**Symbol:** RSR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1835 |
| net_profit_factor | 0.2747 |
| net_win_rate | 0.3907 |
| gross_profit_factor | 0.7401 |
| gross_win_rate | 0.4316 |
| sharpe_ratio | -15.6213 |
| sortino_ratio | -9.5577 |
| max_drawdown | 1.0000 |
| cagr | -0.9930 |
| net_avg_win | 5.2811 |
| net_avg_loss | -12.3314 |
| avg_hold_time_bars | 1.9673 |
| exposure | 0.1641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

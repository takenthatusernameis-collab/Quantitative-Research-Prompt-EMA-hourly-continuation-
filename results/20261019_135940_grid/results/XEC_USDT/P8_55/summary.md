# EMA Hourly Continuation — XEC/USDT P8_55

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.4941 |
| net_win_rate | 0.4452 |
| gross_profit_factor | 0.9384 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -7.4276 |
| sortino_ratio | -3.3689 |
| max_drawdown | 0.9861 |
| cagr | -0.8130 |
| net_avg_win | 20.4308 |
| net_avg_loss | -33.1812 |
| avg_hold_time_bars | 10.6805 |
| exposure | 0.5113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

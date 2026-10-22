# EMA Hourly Continuation — AR/USDT P8_144

**Symbol:** AR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7508 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 0.9777 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -1.7011 |
| sortino_ratio | -0.4600 |
| max_drawdown | 0.4400 |
| cagr | -0.1961 |
| net_avg_win | 70.6315 |
| net_avg_loss | -91.0420 |
| avg_hold_time_bars | 48.1803 |
| exposure | 0.8015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — PHA/USDT P8_144

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.8711 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0068 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.8966 |
| sortino_ratio | -0.2603 |
| max_drawdown | 0.4191 |
| cagr | -0.1158 |
| net_avg_win | 87.2019 |
| net_avg_loss | -100.1074 |
| avg_hold_time_bars | 37.4029 |
| exposure | 0.7005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — FIDA/USDT P55_89

**Symbol:** FIDA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.4094 |
| net_win_rate | 0.4159 |
| gross_profit_factor | 0.7392 |
| gross_win_rate | 0.4277 |
| sharpe_ratio | -6.7157 |
| sortino_ratio | -2.4805 |
| max_drawdown | 0.9505 |
| cagr | -0.6951 |
| net_avg_win | 23.3515 |
| net_avg_loss | -40.6195 |
| avg_hold_time_bars | 4.6224 |
| exposure | 0.1418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

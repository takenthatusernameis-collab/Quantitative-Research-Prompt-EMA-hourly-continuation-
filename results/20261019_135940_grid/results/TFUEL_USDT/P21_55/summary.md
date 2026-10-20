# EMA Hourly Continuation — TFUEL/USDT P21_55

**Symbol:** TFUEL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1072 |
| net_profit_factor | 0.4345 |
| net_win_rate | 0.3909 |
| gross_profit_factor | 0.7813 |
| gross_win_rate | 0.4151 |
| sharpe_ratio | -10.2216 |
| sortino_ratio | -4.7209 |
| max_drawdown | 0.9973 |
| cagr | -0.9045 |
| net_avg_win | 18.2909 |
| net_avg_loss | -27.0094 |
| avg_hold_time_bars | 5.1231 |
| exposure | 0.2485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

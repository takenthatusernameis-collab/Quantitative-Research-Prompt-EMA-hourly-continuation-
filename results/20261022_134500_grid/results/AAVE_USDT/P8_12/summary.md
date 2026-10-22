# EMA Hourly Continuation — AAVE/USDT P8_12

**Symbol:** AAVE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1817 |
| net_profit_factor | 0.1614 |
| net_win_rate | 0.3522 |
| gross_profit_factor | 0.5945 |
| gross_win_rate | 0.3836 |
| sharpe_ratio | -18.9188 |
| sortino_ratio | -11.7511 |
| max_drawdown | 1.0000 |
| cagr | -0.9984 |
| net_avg_win | 3.0072 |
| net_avg_loss | -10.1314 |
| avg_hold_time_bars | 1.9202 |
| exposure | 0.1586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

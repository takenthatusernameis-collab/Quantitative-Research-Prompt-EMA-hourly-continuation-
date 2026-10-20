# EMA Hourly Continuation — PHA/USDT P8_200

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.7521 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9959 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -2.0763 |
| sortino_ratio | -0.6269 |
| max_drawdown | 0.5323 |
| cagr | -0.2535 |
| net_avg_win | 71.7165 |
| net_avg_loss | -90.4264 |
| avg_hold_time_bars | 37.3119 |
| exposure | 0.7666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — MOG/USDT P8_200

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 216 |
| net_profit_factor | 0.9894 |
| net_win_rate | 0.5231 |
| gross_profit_factor | 1.0959 |
| gross_win_rate | 0.5231 |
| sharpe_ratio | -0.0032 |
| sortino_ratio | -0.0007 |
| max_drawdown | 0.0903 |
| cagr | -0.0050 |
| net_avg_win | 93.5401 |
| net_avg_loss | -103.7236 |
| avg_hold_time_bars | 78.0833 |
| exposure | 0.8384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — INJ/USDT P8_21

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1679 |
| net_profit_factor | 0.4496 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.8440 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -10.7945 |
| sortino_ratio | -6.1763 |
| max_drawdown | 0.9996 |
| cagr | -0.9576 |
| net_avg_win | 10.9148 |
| net_avg_loss | -19.5066 |
| avg_hold_time_bars | 2.9595 |
| exposure | 0.2259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — REQ/USDT P8_21

**Symbol:** REQ/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1710 |
| net_profit_factor | 0.3294 |
| net_win_rate | 0.3579 |
| gross_profit_factor | 0.8012 |
| gross_win_rate | 0.4094 |
| sharpe_ratio | -16.7962 |
| sortino_ratio | -10.0199 |
| max_drawdown | 1.0000 |
| cagr | -0.9945 |
| net_avg_win | 8.0245 |
| net_avg_loss | -13.5801 |
| avg_hold_time_bars | 3.3608 |
| exposure | 0.2612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

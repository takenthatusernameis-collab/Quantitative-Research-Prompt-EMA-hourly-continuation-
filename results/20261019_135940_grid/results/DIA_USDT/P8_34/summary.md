# EMA Hourly Continuation — DIA/USDT P8_34

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1291 |
| net_profit_factor | 0.4702 |
| net_win_rate | 0.4454 |
| gross_profit_factor | 0.8215 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -7.9852 |
| sortino_ratio | -4.0305 |
| max_drawdown | 0.9928 |
| cagr | -0.8578 |
| net_avg_win | 15.3209 |
| net_avg_loss | -26.1684 |
| avg_hold_time_bars | 6.1317 |
| exposure | 0.3582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — KNC/USDT P8_26

**Symbol:** KNC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1353 |
| net_profit_factor | 0.4139 |
| net_win_rate | 0.4220 |
| gross_profit_factor | 0.8867 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -10.5546 |
| sortino_ratio | -5.4814 |
| max_drawdown | 0.9990 |
| cagr | -0.9349 |
| net_avg_win | 12.3556 |
| net_avg_loss | -21.7961 |
| avg_hold_time_bars | 5.1397 |
| exposure | 0.3161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

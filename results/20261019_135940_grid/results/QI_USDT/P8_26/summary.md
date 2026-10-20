# EMA Hourly Continuation — QI/USDT P8_26

**Symbol:** QI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1329 |
| net_profit_factor | 0.4470 |
| net_win_rate | 0.4439 |
| gross_profit_factor | 0.8264 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -8.9031 |
| sortino_ratio | -4.5737 |
| max_drawdown | 0.9964 |
| cagr | -0.8930 |
| net_avg_win | 13.6490 |
| net_avg_loss | -24.3806 |
| avg_hold_time_bars | 4.8074 |
| exposure | 0.2891 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

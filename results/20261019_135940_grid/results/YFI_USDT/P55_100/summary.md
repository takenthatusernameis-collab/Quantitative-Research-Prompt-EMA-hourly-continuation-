# EMA Hourly Continuation — YFI/USDT P55_100

**Symbol:** YFI/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.4051 |
| net_win_rate | 0.4232 |
| gross_profit_factor | 0.9082 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -7.8013 |
| sortino_ratio | -2.9727 |
| max_drawdown | 0.9771 |
| cagr | -0.7724 |
| net_avg_win | 21.7191 |
| net_avg_loss | -39.3456 |
| avg_hold_time_bars | 5.3154 |
| exposure | 0.1739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

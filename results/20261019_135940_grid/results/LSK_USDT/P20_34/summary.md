# EMA Hourly Continuation — LSK/USDT P20_34

**Symbol:** LSK/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 932 |
| net_profit_factor | 0.4039 |
| net_win_rate | 0.4313 |
| gross_profit_factor | 0.8869 |
| gross_win_rate | 0.4603 |
| sharpe_ratio | -8.5670 |
| sortino_ratio | -3.7291 |
| max_drawdown | 0.9899 |
| cagr | -0.8377 |
| net_avg_win | 16.6796 |
| net_avg_loss | -31.3230 |
| avg_hold_time_bars | 4.0086 |
| exposure | 0.1698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

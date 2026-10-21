# EMA Hourly Continuation — FLR/USDT P20_26

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 211 |
| net_profit_factor | 0.4448 |
| net_win_rate | 0.4028 |
| gross_profit_factor | 0.6743 |
| gross_win_rate | 0.4028 |
| sharpe_ratio | -3.6335 |
| sortino_ratio | -0.7558 |
| max_drawdown | 0.5950 |
| cagr | -0.2951 |
| net_avg_win | 55.0863 |
| net_avg_loss | -83.5448 |
| avg_hold_time_bars | 4.9005 |
| exposure | 0.0470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

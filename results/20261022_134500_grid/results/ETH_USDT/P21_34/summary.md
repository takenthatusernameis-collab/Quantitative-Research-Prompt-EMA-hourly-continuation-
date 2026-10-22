# EMA Hourly Continuation — ETH/USDT P21_34

**Symbol:** ETH/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1091 |
| net_profit_factor | 0.1843 |
| net_win_rate | 0.3364 |
| gross_profit_factor | 0.8092 |
| gross_win_rate | 0.4253 |
| sharpe_ratio | -15.0566 |
| sortino_ratio | -7.3745 |
| max_drawdown | 1.0000 |
| cagr | -0.9809 |
| net_avg_win | 6.1553 |
| net_avg_loss | -16.9317 |
| avg_hold_time_bars | 2.5490 |
| exposure | 0.1264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

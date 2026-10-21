# EMA Hourly Continuation — BTT/USDT P26_34

**Symbol:** BTT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 213 |
| net_profit_factor | 0.3620 |
| net_win_rate | 0.3944 |
| gross_profit_factor | 0.7233 |
| gross_win_rate | 0.3991 |
| sharpe_ratio | -4.9173 |
| sortino_ratio | -1.0554 |
| max_drawdown | 0.7199 |
| cagr | -0.3919 |
| net_avg_win | 48.1713 |
| net_avg_loss | -86.6573 |
| avg_hold_time_bars | 5.8779 |
| exposure | 0.0569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

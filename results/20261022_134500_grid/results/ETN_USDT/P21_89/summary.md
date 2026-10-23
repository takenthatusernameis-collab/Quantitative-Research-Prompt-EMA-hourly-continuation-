# EMA Hourly Continuation — ETN/USDT P21_89

**Symbol:** ETN/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.3704 |
| net_win_rate | 0.3627 |
| gross_profit_factor | 0.5741 |
| gross_win_rate | 0.3796 |
| sharpe_ratio | -8.8774 |
| sortino_ratio | -3.6518 |
| max_drawdown | 0.9767 |
| cagr | -0.8321 |
| net_avg_win | 22.1786 |
| net_avg_loss | -34.0858 |
| avg_hold_time_bars | 8.8571 |
| exposure | 0.3435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

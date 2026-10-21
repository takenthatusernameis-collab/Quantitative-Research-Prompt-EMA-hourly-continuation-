# EMA Hourly Continuation — BAT/USDT P20_89

**Symbol:** BAT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.7601 |
| net_win_rate | 0.5009 |
| gross_profit_factor | 1.0145 |
| gross_win_rate | 0.5009 |
| sharpe_ratio | -2.0811 |
| sortino_ratio | -0.7024 |
| max_drawdown | 0.5911 |
| cagr | -0.2756 |
| net_avg_win | 63.2337 |
| net_avg_loss | -83.4960 |
| avg_hold_time_bars | 15.4541 |
| exposure | 0.3899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

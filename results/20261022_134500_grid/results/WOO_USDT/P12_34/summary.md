# EMA Hourly Continuation — WOO/USDT P12_34

**Symbol:** WOO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1243 |
| net_profit_factor | 0.5764 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 1.0172 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -7.2886 |
| sortino_ratio | -3.6270 |
| max_drawdown | 0.9880 |
| cagr | -0.8257 |
| net_avg_win | 23.3341 |
| net_avg_loss | -34.9565 |
| avg_hold_time_bars | 4.4529 |
| exposure | 0.2516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

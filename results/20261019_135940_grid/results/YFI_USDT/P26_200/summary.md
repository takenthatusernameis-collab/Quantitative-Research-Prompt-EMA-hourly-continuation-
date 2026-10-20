# EMA Hourly Continuation — YFI/USDT P26_200

**Symbol:** YFI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.6568 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 1.0305 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -2.5851 |
| sortino_ratio | -0.7494 |
| max_drawdown | 0.6049 |
| cagr | -0.2953 |
| net_avg_win | 53.4391 |
| net_avg_loss | -81.7554 |
| avg_hold_time_bars | 30.6826 |
| exposure | 0.5817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

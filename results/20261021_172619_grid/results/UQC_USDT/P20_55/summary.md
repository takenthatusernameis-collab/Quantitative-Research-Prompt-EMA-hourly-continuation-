# EMA Hourly Continuation — UQC/USDT P20_55

**Symbol:** UQC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.3848 |
| net_win_rate | 0.3185 |
| gross_profit_factor | 0.5779 |
| gross_win_rate | 0.3296 |
| sharpe_ratio | -5.3049 |
| sortino_ratio | -1.2202 |
| max_drawdown | 0.7742 |
| cagr | -0.4435 |
| net_avg_win | 56.1446 |
| net_avg_loss | -68.1951 |
| avg_hold_time_bars | 43.1407 |
| exposure | 0.5272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

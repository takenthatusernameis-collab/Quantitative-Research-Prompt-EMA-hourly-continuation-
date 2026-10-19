# EMA Hourly Continuation — XDC/USDT P26_50

**Symbol:** XDC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1042 |
| net_profit_factor | 0.1565 |
| net_win_rate | 0.3656 |
| gross_profit_factor | 0.4944 |
| gross_win_rate | 0.4184 |
| sharpe_ratio | -13.0341 |
| sortino_ratio | -6.0851 |
| max_drawdown | 0.9997 |
| cagr | -0.9616 |
| net_avg_win | 4.8672 |
| net_avg_loss | -17.9298 |
| avg_hold_time_bars | 3.7226 |
| exposure | 0.1763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — XMR/USDT P21_55

**Symbol:** XMR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1365 |
| net_profit_factor | 0.2810 |
| net_win_rate | 0.3993 |
| gross_profit_factor | 0.7248 |
| gross_win_rate | 0.4227 |
| sharpe_ratio | -12.1987 |
| sortino_ratio | -6.3841 |
| max_drawdown | 0.9997 |
| cagr | -0.9622 |
| net_avg_win | 7.1686 |
| net_avg_loss | -16.9563 |
| avg_hold_time_bars | 3.2652 |
| exposure | 0.2026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

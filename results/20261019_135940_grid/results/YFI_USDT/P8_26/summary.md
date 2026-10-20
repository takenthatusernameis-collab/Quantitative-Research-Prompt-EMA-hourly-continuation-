# EMA Hourly Continuation — YFI/USDT P8_26

**Symbol:** YFI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1673 |
| net_profit_factor | 0.3045 |
| net_win_rate | 0.4250 |
| gross_profit_factor | 0.8686 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -12.9725 |
| sortino_ratio | -7.5000 |
| max_drawdown | 0.9999 |
| cagr | -0.9780 |
| net_avg_win | 6.1569 |
| net_avg_loss | -14.9448 |
| avg_hold_time_bars | 3.9522 |
| exposure | 0.2992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

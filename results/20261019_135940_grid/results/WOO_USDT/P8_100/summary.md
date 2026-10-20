# EMA Hourly Continuation — WOO/USDT P8_100

**Symbol:** WOO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.6951 |
| net_win_rate | 0.4696 |
| gross_profit_factor | 0.9666 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -3.3752 |
| sortino_ratio | -1.1953 |
| max_drawdown | 0.7641 |
| cagr | -0.4286 |
| net_avg_win | 58.5130 |
| net_avg_loss | -74.5490 |
| avg_hold_time_bars | 23.8131 |
| exposure | 0.6776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

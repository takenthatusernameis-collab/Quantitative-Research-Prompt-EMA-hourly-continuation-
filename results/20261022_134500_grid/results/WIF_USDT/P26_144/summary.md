# EMA Hourly Continuation — WIF/USDT P26_144

**Symbol:** WIF/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.6692 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.8788 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -2.8459 |
| sortino_ratio | -0.9208 |
| max_drawdown | 0.6817 |
| cagr | -0.3500 |
| net_avg_win | 54.3488 |
| net_avg_loss | -72.3891 |
| avg_hold_time_bars | 19.2375 |
| exposure | 0.4565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

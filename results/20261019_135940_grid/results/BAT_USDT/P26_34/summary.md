# EMA Hourly Continuation — BAT/USDT P26_34

**Symbol:** BAT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1077 |
| net_profit_factor | 0.2036 |
| net_win_rate | 0.3863 |
| gross_profit_factor | 0.6958 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -12.0757 |
| sortino_ratio | -5.7287 |
| max_drawdown | 0.9994 |
| cagr | -0.9462 |
| net_avg_win | 6.1429 |
| net_avg_loss | -18.9848 |
| avg_hold_time_bars | 2.5562 |
| exposure | 0.1251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

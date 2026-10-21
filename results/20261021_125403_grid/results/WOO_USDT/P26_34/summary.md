# EMA Hourly Continuation — WOO/USDT P26_34

**Symbol:** WOO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.6956 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 0.9840 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -1.9367 |
| sortino_ratio | -0.4481 |
| max_drawdown | 0.4403 |
| cagr | -0.1861 |
| net_avg_win | 72.0714 |
| net_avg_loss | -100.4732 |
| avg_hold_time_bars | 4.7385 |
| exposure | 0.0560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

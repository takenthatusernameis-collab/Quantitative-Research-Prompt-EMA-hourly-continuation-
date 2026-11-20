# EMA Hourly Continuation — P2P/USDT P21_55

**Symbol:** P2P/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 883 |
| net_profit_factor | 0.3153 |
| net_win_rate | 0.3375 |
| gross_profit_factor | 0.4964 |
| gross_win_rate | 0.3409 |
| sharpe_ratio | -9.0974 |
| sortino_ratio | -3.7914 |
| max_drawdown | 0.9903 |
| cagr | -0.8421 |
| net_avg_win | 15.3034 |
| net_avg_loss | -24.7238 |
| avg_hold_time_bars | 6.2084 |
| exposure | 0.2492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

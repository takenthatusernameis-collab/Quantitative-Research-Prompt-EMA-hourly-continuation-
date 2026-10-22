# EMA Hourly Continuation — SUN/USDT P21_50

**Symbol:** SUN/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 843 |
| net_profit_factor | 0.2797 |
| net_win_rate | 0.3523 |
| gross_profit_factor | 0.7973 |
| gross_win_rate | 0.4187 |
| sharpe_ratio | -11.8392 |
| sortino_ratio | -4.9945 |
| max_drawdown | 0.9986 |
| cagr | -0.9268 |
| net_avg_win | 13.0585 |
| net_avg_loss | -25.3933 |
| avg_hold_time_bars | 6.8019 |
| exposure | 0.2595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ZRX/USDT P12_89

**Symbol:** ZRX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7375 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9425 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -2.2989 |
| sortino_ratio | -0.7561 |
| max_drawdown | 0.6031 |
| cagr | -0.2954 |
| net_avg_win | 63.4489 |
| net_avg_loss | -81.3224 |
| avg_hold_time_bars | 22.5535 |
| exposure | 0.5464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

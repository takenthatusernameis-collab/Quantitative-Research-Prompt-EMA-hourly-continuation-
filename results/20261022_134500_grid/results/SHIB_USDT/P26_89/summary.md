# EMA Hourly Continuation — SHIB/USDT P26_89

**Symbol:** SHIB/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 749 |
| net_profit_factor | 0.5931 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.9894 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -5.4381 |
| sortino_ratio | -2.0995 |
| max_drawdown | 0.9243 |
| cagr | -0.6381 |
| net_avg_win | 38.4031 |
| net_avg_loss | -56.7979 |
| avg_hold_time_bars | 7.8491 |
| exposure | 0.2672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

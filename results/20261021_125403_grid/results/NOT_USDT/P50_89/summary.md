# EMA Hourly Continuation — NOT/USDT P50_89

**Symbol:** NOT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.7734 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 0.9972 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -1.4027 |
| sortino_ratio | -0.3638 |
| max_drawdown | 0.3588 |
| cagr | -0.1543 |
| net_avg_win | 71.8117 |
| net_avg_loss | -94.0300 |
| avg_hold_time_bars | 7.3006 |
| exposure | 0.1084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

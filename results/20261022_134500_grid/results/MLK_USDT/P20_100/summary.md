# EMA Hourly Continuation — MLK/USDT P20_100

**Symbol:** MLK/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 988 |
| net_profit_factor | 0.3342 |
| net_win_rate | 0.2955 |
| gross_profit_factor | 0.5704 |
| gross_win_rate | 0.3057 |
| sharpe_ratio | -12.3732 |
| sortino_ratio | -5.5089 |
| max_drawdown | 0.9991 |
| cagr | -0.9370 |
| net_avg_win | 17.1704 |
| net_avg_loss | -21.5580 |
| avg_hold_time_bars | 8.8087 |
| exposure | 0.3939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

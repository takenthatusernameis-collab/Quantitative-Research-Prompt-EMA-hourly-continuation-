# EMA Hourly Continuation — FLR/USDT P50_89

**Symbol:** FLR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.5859 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8308 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -3.0179 |
| sortino_ratio | -0.8109 |
| max_drawdown | 0.6135 |
| cagr | -0.3106 |
| net_avg_win | 52.7007 |
| net_avg_loss | -77.1639 |
| avg_hold_time_bars | 6.7989 |
| exposure | 0.1091 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

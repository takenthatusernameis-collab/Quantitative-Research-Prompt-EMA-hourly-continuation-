# EMA Hourly Continuation — EWT/USDT P20_55

**Symbol:** EWT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 871 |
| net_profit_factor | 0.4763 |
| net_win_rate | 0.4259 |
| gross_profit_factor | 0.7980 |
| gross_win_rate | 0.4305 |
| sharpe_ratio | -7.3939 |
| sortino_ratio | -3.0460 |
| max_drawdown | 0.9787 |
| cagr | -0.7826 |
| net_avg_win | 23.9859 |
| net_avg_loss | -37.3644 |
| avg_hold_time_bars | 5.8829 |
| exposure | 0.2329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

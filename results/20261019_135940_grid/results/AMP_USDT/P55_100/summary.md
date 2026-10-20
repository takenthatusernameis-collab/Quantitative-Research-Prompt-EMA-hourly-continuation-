# EMA Hourly Continuation — AMP/USDT P55_100

**Symbol:** AMP/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 876 |
| net_profit_factor | 0.2899 |
| net_win_rate | 0.3539 |
| gross_profit_factor | 0.6070 |
| gross_win_rate | 0.3836 |
| sharpe_ratio | -10.6591 |
| sortino_ratio | -4.5085 |
| max_drawdown | 0.9968 |
| cagr | -0.8959 |
| net_avg_win | 13.1236 |
| net_avg_loss | -24.7954 |
| avg_hold_time_bars | 5.0753 |
| exposure | 0.2021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

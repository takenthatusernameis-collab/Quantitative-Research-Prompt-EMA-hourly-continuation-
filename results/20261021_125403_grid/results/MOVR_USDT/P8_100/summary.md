# EMA Hourly Continuation — MOVR/USDT P8_100

**Symbol:** MOVR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.7126 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.8703 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -2.3828 |
| sortino_ratio | -0.7566 |
| max_drawdown | 0.5899 |
| cagr | -0.2941 |
| net_avg_win | 62.2902 |
| net_avg_loss | -75.6758 |
| avg_hold_time_bars | 28.9540 |
| exposure | 0.6580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ILV/USDT P12_100

**Symbol:** ILV/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.7129 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 1.0235 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.9917 |
| sortino_ratio | -1.0771 |
| max_drawdown | 0.7272 |
| cagr | -0.3997 |
| net_avg_win | 55.5250 |
| net_avg_loss | -76.9374 |
| avg_hold_time_bars | 18.9523 |
| exposure | 0.5600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

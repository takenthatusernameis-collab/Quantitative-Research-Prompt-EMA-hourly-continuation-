# EMA Hourly Continuation — JTO/USDT P8_144

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.7691 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9955 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -1.7989 |
| sortino_ratio | -0.5476 |
| max_drawdown | 0.5288 |
| cagr | -0.2270 |
| net_avg_win | 69.5486 |
| net_avg_loss | -87.7367 |
| avg_hold_time_bars | 35.4795 |
| exposure | 0.7467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

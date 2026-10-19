# EMA Hourly Continuation — TAO/USDT P12_21

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1485 |
| net_profit_factor | 0.3560 |
| net_win_rate | 0.4175 |
| gross_profit_factor | 0.7510 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -12.1001 |
| sortino_ratio | -6.5928 |
| max_drawdown | 0.9998 |
| cagr | -0.9661 |
| net_avg_win | 8.9139 |
| net_avg_loss | -17.9475 |
| avg_hold_time_bars | 2.1165 |
| exposure | 0.1429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

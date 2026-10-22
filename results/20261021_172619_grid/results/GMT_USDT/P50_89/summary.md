# EMA Hourly Continuation — GMT/USDT P50_89

**Symbol:** GMT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.6424 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8609 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -2.6697 |
| sortino_ratio | -0.6987 |
| max_drawdown | 0.5667 |
| cagr | -0.2744 |
| net_avg_win | 64.5127 |
| net_avg_loss | -84.5150 |
| avg_hold_time_bars | 7.1691 |
| exposure | 0.1098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — TAO/USDT P50_89

**Symbol:** TAO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.9200 |
| net_win_rate | 0.5377 |
| gross_profit_factor | 1.1478 |
| gross_win_rate | 0.5377 |
| sharpe_ratio | -0.3782 |
| sortino_ratio | -0.0935 |
| max_drawdown | 0.2073 |
| cagr | -0.0457 |
| net_avg_win | 81.2070 |
| net_avg_loss | -102.6495 |
| avg_hold_time_bars | 8.4795 |
| exposure | 0.1125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

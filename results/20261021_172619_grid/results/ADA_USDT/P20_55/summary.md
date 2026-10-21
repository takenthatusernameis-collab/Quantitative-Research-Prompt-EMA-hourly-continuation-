# EMA Hourly Continuation — ADA/USDT P20_55

**Symbol:** ADA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.7855 |
| net_win_rate | 0.5183 |
| gross_profit_factor | 1.0642 |
| gross_win_rate | 0.5183 |
| sharpe_ratio | -1.6150 |
| sortino_ratio | -0.5157 |
| max_drawdown | 0.4682 |
| cagr | -0.2107 |
| net_avg_win | 64.3250 |
| net_avg_loss | -88.1131 |
| avg_hold_time_bars | 8.7622 |
| exposure | 0.1960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

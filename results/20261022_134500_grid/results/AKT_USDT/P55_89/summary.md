# EMA Hourly Continuation — AKT/USDT P55_89

**Symbol:** AKT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.6163 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 1.1124 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -4.6359 |
| sortino_ratio | -1.6916 |
| max_drawdown | 0.8799 |
| cagr | -0.5643 |
| net_avg_win | 42.6291 |
| net_avg_loss | -66.1636 |
| avg_hold_time_bars | 4.2119 |
| exposure | 0.1292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

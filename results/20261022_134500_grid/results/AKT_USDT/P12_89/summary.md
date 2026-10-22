# EMA Hourly Continuation — AKT/USDT P12_89

**Symbol:** AKT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.6053 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.9082 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -4.2623 |
| sortino_ratio | -1.6171 |
| max_drawdown | 0.8629 |
| cagr | -0.5424 |
| net_avg_win | 38.4290 |
| net_avg_loss | -55.6962 |
| avg_hold_time_bars | 15.2561 |
| exposure | 0.5090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

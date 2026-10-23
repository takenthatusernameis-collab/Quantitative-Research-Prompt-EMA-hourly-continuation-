# EMA Hourly Continuation — CTC/USDT P50_144

**Symbol:** CTC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.6110 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 1.0401 |
| gross_win_rate | 0.5163 |
| sharpe_ratio | -3.4793 |
| sortino_ratio | -1.1172 |
| max_drawdown | 0.7597 |
| cagr | -0.4178 |
| net_avg_win | 45.4001 |
| net_avg_loss | -71.7952 |
| avg_hold_time_bars | 11.7801 |
| exposure | 0.2800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

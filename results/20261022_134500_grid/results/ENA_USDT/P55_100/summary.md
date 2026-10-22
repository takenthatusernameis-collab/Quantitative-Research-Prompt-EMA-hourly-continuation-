# EMA Hourly Continuation — ENA/USDT P55_100

**Symbol:** ENA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.6021 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8704 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -3.9100 |
| sortino_ratio | -1.3163 |
| max_drawdown | 0.8012 |
| cagr | -0.4621 |
| net_avg_win | 45.5811 |
| net_avg_loss | -65.2483 |
| avg_hold_time_bars | 4.9647 |
| exposure | 0.1277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

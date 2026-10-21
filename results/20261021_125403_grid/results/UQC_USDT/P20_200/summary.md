# EMA Hourly Continuation — UQC/USDT P20_200

**Symbol:** UQC/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 183 |
| net_profit_factor | 0.3452 |
| net_win_rate | 0.2896 |
| gross_profit_factor | 0.4304 |
| gross_win_rate | 0.2951 |
| sharpe_ratio | -4.4058 |
| sortino_ratio | -0.8304 |
| max_drawdown | 0.6271 |
| cagr | -0.3237 |
| net_avg_win | 62.3879 |
| net_avg_loss | -73.6744 |
| avg_hold_time_bars | 87.1093 |
| exposure | 0.7215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

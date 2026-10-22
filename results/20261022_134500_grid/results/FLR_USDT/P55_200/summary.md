# EMA Hourly Continuation — FLR/USDT P55_200

**Symbol:** FLR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.6414 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9884 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -3.2784 |
| sortino_ratio | -1.0401 |
| max_drawdown | 0.7253 |
| cagr | -0.3926 |
| net_avg_win | 51.2866 |
| net_avg_loss | -77.4744 |
| avg_hold_time_bars | 13.8893 |
| exposure | 0.3195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

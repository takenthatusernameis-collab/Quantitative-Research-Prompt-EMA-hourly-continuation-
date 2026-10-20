# EMA Hourly Continuation — DAG/USDT P34_50

**Symbol:** DAG/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 874 |
| net_profit_factor | 0.2838 |
| net_win_rate | 0.3730 |
| gross_profit_factor | 0.5637 |
| gross_win_rate | 0.3890 |
| sharpe_ratio | -10.5131 |
| sortino_ratio | -4.4058 |
| max_drawdown | 0.9971 |
| cagr | -0.9019 |
| net_avg_win | 12.1171 |
| net_avg_loss | -25.4029 |
| avg_hold_time_bars | 2.3993 |
| exposure | 0.0953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

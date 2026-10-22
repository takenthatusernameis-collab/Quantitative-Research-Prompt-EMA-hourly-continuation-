# EMA Hourly Continuation — BSV/USDT P20_26

**Symbol:** BSV/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1333 |
| net_profit_factor | 0.1410 |
| net_win_rate | 0.3158 |
| gross_profit_factor | 0.5811 |
| gross_win_rate | 0.3923 |
| sharpe_ratio | -17.3815 |
| sortino_ratio | -9.4661 |
| max_drawdown | 1.0000 |
| cagr | -0.9940 |
| net_avg_win | 3.8990 |
| net_avg_loss | -12.7648 |
| avg_hold_time_bars | 2.0863 |
| exposure | 0.1264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

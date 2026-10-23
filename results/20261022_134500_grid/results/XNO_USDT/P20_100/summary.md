# EMA Hourly Continuation — XNO/USDT P20_100

**Symbol:** XNO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 839 |
| net_profit_factor | 0.5196 |
| net_win_rate | 0.4148 |
| gross_profit_factor | 0.7933 |
| gross_win_rate | 0.4207 |
| sharpe_ratio | -6.7786 |
| sortino_ratio | -2.7607 |
| max_drawdown | 0.9647 |
| cagr | -0.7356 |
| net_avg_win | 29.9741 |
| net_avg_loss | -40.8899 |
| avg_hold_time_bars | 10.4863 |
| exposure | 0.3999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

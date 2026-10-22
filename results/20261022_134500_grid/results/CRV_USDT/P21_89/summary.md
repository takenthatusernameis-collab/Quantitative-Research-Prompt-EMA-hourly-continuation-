# EMA Hourly Continuation — CRV/USDT P21_89

**Symbol:** CRV/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 748 |
| net_profit_factor | 0.6490 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 0.9865 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -3.9570 |
| sortino_ratio | -1.5276 |
| max_drawdown | 0.8484 |
| cagr | -0.5160 |
| net_avg_win | 42.7012 |
| net_avg_loss | -62.0369 |
| avg_hold_time_bars | 9.6310 |
| exposure | 0.3275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

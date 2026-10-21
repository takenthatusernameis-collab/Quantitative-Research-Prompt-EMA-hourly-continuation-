# EMA Hourly Continuation — BSV/USDT P34_200

**Symbol:** BSV/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.6901 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8605 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -2.1524 |
| sortino_ratio | -0.5503 |
| max_drawdown | 0.4825 |
| cagr | -0.2233 |
| net_avg_win | 69.7447 |
| net_avg_loss | -86.6284 |
| avg_hold_time_bars | 35.2923 |
| exposure | 0.5214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

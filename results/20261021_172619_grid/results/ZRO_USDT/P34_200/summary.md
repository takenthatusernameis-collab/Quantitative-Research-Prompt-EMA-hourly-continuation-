# EMA Hourly Continuation — ZRO/USDT P34_200

**Symbol:** ZRO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.8265 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9482 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -0.9951 |
| sortino_ratio | -0.2482 |
| max_drawdown | 0.2733 |
| cagr | -0.1098 |
| net_avg_win | 81.4659 |
| net_avg_loss | -94.4830 |
| avg_hold_time_bars | 34.2852 |
| exposure | 0.4766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

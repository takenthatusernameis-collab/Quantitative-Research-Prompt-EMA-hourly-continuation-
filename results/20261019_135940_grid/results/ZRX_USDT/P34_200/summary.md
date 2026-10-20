# EMA Hourly Continuation — ZRX/USDT P34_200

**Symbol:** ZRX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.5817 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.8221 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -3.3230 |
| sortino_ratio | -0.9446 |
| max_drawdown | 0.6955 |
| cagr | -0.3632 |
| net_avg_win | 50.6906 |
| net_avg_loss | -72.6885 |
| avg_hold_time_bars | 27.6308 |
| exposure | 0.5137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — LTC/USDT P89_200

**Symbol:** LTC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.5155 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.7292 |
| gross_win_rate | 0.4327 |
| sharpe_ratio | -3.1288 |
| sortino_ratio | -0.7388 |
| max_drawdown | 0.5821 |
| cagr | -0.2882 |
| net_avg_win | 51.3428 |
| net_avg_loss | -75.9730 |
| avg_hold_time_bars | 13.3564 |
| exposure | 0.1670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — TAO/USDT P34_200

**Symbol:** TAO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.9259 |
| net_win_rate | 0.5176 |
| gross_profit_factor | 1.0689 |
| gross_win_rate | 0.5176 |
| sharpe_ratio | -0.3569 |
| sortino_ratio | -0.0865 |
| max_drawdown | 0.1666 |
| cagr | -0.0425 |
| net_avg_win | 87.9164 |
| net_avg_loss | -101.8788 |
| avg_hold_time_bars | 36.4190 |
| exposure | 0.4701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

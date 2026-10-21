# EMA Hourly Continuation — XNO/USDT P50_200

**Symbol:** XNO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.6402 |
| net_win_rate | 0.4402 |
| gross_profit_factor | 0.7985 |
| gross_win_rate | 0.4402 |
| sharpe_ratio | -2.7713 |
| sortino_ratio | -0.7530 |
| max_drawdown | 0.5811 |
| cagr | -0.2928 |
| net_avg_win | 63.8266 |
| net_avg_loss | -78.4019 |
| avg_hold_time_bars | 20.8342 |
| exposure | 0.3485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

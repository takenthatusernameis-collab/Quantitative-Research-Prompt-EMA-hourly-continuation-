# EMA Hourly Continuation — SUSHI/USDT P8_200

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.7621 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9060 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -1.3700 |
| sortino_ratio | -0.3258 |
| max_drawdown | 0.3283 |
| cagr | -0.1402 |
| net_avg_win | 75.7212 |
| net_avg_loss | -90.5735 |
| avg_hold_time_bars | 63.2669 |
| exposure | 0.8045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

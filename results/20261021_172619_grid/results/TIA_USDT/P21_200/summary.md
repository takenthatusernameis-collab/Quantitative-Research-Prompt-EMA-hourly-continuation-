# EMA Hourly Continuation — TIA/USDT P21_200

**Symbol:** TIA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.7539 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8530 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -1.4272 |
| sortino_ratio | -0.3185 |
| max_drawdown | 0.3721 |
| cagr | -0.1373 |
| net_avg_win | 83.3033 |
| net_avg_loss | -94.0008 |
| avg_hold_time_bars | 59.3710 |
| exposure | 0.6693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

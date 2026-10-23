# EMA Hourly Continuation — LPT/USDT P12_34

**Symbol:** LPT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1329 |
| net_profit_factor | 0.5090 |
| net_win_rate | 0.4289 |
| gross_profit_factor | 0.8546 |
| gross_win_rate | 0.4402 |
| sharpe_ratio | -9.6151 |
| sortino_ratio | -4.9259 |
| max_drawdown | 0.9979 |
| cagr | -0.9138 |
| net_avg_win | 18.1462 |
| net_avg_loss | -26.7749 |
| avg_hold_time_bars | 4.3461 |
| exposure | 0.2625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

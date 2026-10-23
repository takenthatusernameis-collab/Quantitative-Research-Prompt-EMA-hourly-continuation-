# EMA Hourly Continuation — ONT/USDT P8_34

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1382 |
| net_profit_factor | 0.5001 |
| net_win_rate | 0.4219 |
| gross_profit_factor | 0.9239 |
| gross_win_rate | 0.4414 |
| sharpe_ratio | -10.0469 |
| sortino_ratio | -5.2117 |
| max_drawdown | 0.9987 |
| cagr | -0.9278 |
| net_avg_win | 17.1347 |
| net_avg_loss | -25.0017 |
| avg_hold_time_bars | 5.2337 |
| exposure | 0.3273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

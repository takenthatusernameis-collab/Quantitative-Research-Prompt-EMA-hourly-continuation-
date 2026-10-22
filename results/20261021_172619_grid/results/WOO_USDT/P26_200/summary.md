# EMA Hourly Continuation — WOO/USDT P26_200

**Symbol:** WOO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.9570 |
| net_win_rate | 0.5326 |
| gross_profit_factor | 1.1376 |
| gross_win_rate | 0.5361 |
| sharpe_ratio | -0.2037 |
| sortino_ratio | -0.0501 |
| max_drawdown | 0.2617 |
| cagr | -0.0273 |
| net_avg_win | 96.4462 |
| net_avg_loss | -114.8553 |
| avg_hold_time_bars | 45.2612 |
| exposure | 0.5987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

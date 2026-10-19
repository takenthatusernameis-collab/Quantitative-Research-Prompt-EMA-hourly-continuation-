# EMA Hourly Continuation — MANA/USDT P21_200

**Symbol:** MANA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.6890 |
| net_win_rate | 0.4986 |
| gross_profit_factor | 1.0333 |
| gross_win_rate | 0.5072 |
| sharpe_ratio | -2.2253 |
| sortino_ratio | -0.5820 |
| max_drawdown | 0.5338 |
| cagr | -0.2459 |
| net_avg_win | 64.6412 |
| net_avg_loss | -93.2877 |
| avg_hold_time_bars | 41.7049 |
| exposure | 0.6616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

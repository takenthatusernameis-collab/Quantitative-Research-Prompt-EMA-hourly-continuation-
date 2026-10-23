# EMA Hourly Continuation — LPT/USDT P12_200

**Symbol:** LPT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.6300 |
| net_win_rate | 0.4534 |
| gross_profit_factor | 0.8506 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -3.0200 |
| sortino_ratio | -0.8546 |
| max_drawdown | 0.6755 |
| cagr | -0.3339 |
| net_avg_win | 58.8553 |
| net_avg_loss | -77.5072 |
| avg_hold_time_bars | 39.4534 |
| exposure | 0.7317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

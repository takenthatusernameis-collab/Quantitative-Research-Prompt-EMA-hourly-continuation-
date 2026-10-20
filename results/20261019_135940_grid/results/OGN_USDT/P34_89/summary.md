# EMA Hourly Continuation — OGN/USDT P34_89

**Symbol:** OGN/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.5072 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8911 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -5.9807 |
| sortino_ratio | -2.2315 |
| max_drawdown | 0.9395 |
| cagr | -0.6637 |
| net_avg_win | 30.7781 |
| net_avg_loss | -48.2067 |
| avg_hold_time_bars | 8.2716 |
| exposure | 0.2646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

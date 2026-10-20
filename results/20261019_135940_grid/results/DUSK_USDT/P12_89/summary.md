# EMA Hourly Continuation — DUSK/USDT P12_89

**Symbol:** DUSK/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.6426 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.9032 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -4.1741 |
| sortino_ratio | -1.5934 |
| max_drawdown | 0.8609 |
| cagr | -0.5267 |
| net_avg_win | 46.1645 |
| net_avg_loss | -59.1175 |
| avg_hold_time_bars | 16.3352 |
| exposure | 0.5428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

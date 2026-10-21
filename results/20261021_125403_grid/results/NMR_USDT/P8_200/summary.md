# EMA Hourly Continuation — NMR/USDT P8_200

**Symbol:** NMR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.9051 |
| net_win_rate | 0.5231 |
| gross_profit_factor | 1.0746 |
| gross_win_rate | 0.5231 |
| sharpe_ratio | -0.5007 |
| sortino_ratio | -0.1338 |
| max_drawdown | 0.2644 |
| cagr | -0.0638 |
| net_avg_win | 80.3429 |
| net_avg_loss | -97.3798 |
| avg_hold_time_bars | 48.4538 |
| exposure | 0.7620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

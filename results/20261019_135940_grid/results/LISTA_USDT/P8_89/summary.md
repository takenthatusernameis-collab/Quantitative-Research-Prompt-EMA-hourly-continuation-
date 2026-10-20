# EMA Hourly Continuation — LISTA/USDT P8_89

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.7154 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9650 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -3.0074 |
| sortino_ratio | -1.1207 |
| max_drawdown | 0.7083 |
| cagr | -0.4092 |
| net_avg_win | 57.3629 |
| net_avg_loss | -73.5366 |
| avg_hold_time_bars | 19.5139 |
| exposure | 0.6183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ORDI/USDT P8_89

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 780 |
| net_profit_factor | 0.6280 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.8937 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -4.8805 |
| sortino_ratio | -1.9185 |
| max_drawdown | 0.9043 |
| cagr | -0.5996 |
| net_avg_win | 42.9035 |
| net_avg_loss | -56.7697 |
| avg_hold_time_bars | 17.5526 |
| exposure | 0.6223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

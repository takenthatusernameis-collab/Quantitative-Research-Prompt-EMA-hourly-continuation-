# EMA Hourly Continuation — DIA/USDT P21_144

**Symbol:** DIA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.7688 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9436 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -1.6394 |
| sortino_ratio | -0.4757 |
| max_drawdown | 0.5043 |
| cagr | -0.1980 |
| net_avg_win | 69.9084 |
| net_avg_loss | -87.0762 |
| avg_hold_time_bars | 27.0120 |
| exposure | 0.5073 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CHZ/USDT P50_55

**Symbol:** CHZ/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 790 |
| net_profit_factor | 0.2049 |
| net_win_rate | 0.3392 |
| gross_profit_factor | 0.7204 |
| gross_win_rate | 0.4038 |
| sharpe_ratio | -12.9257 |
| sortino_ratio | -5.4175 |
| max_drawdown | 0.9994 |
| cagr | -0.9492 |
| net_avg_win | 9.6132 |
| net_avg_loss | -24.0818 |
| avg_hold_time_bars | 1.7468 |
| exposure | 0.0627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

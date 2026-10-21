# EMA Hourly Continuation — BABYDOGE/USDT P12_55

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 67 |
| net_profit_factor | 0.9988 |
| net_win_rate | 0.5224 |
| gross_profit_factor | 1.0828 |
| gross_win_rate | 0.5224 |
| sharpe_ratio | 0.0226 |
| sortino_ratio | 0.0027 |
| max_drawdown | 0.0575 |
| cagr | -0.0002 |
| net_avg_win | 94.6769 |
| net_avg_loss | -103.6816 |
| avg_hold_time_bars | 26.8806 |
| exposure | 0.0815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — HTX/USDT P12_144

**Symbol:** HTX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.4173 |
| net_win_rate | 0.3723 |
| gross_profit_factor | 0.9242 |
| gross_win_rate | 0.4252 |
| sharpe_ratio | -8.5981 |
| sortino_ratio | -2.8716 |
| max_drawdown | 0.9813 |
| cagr | -0.7890 |
| net_avg_win | 34.4185 |
| net_avg_loss | -48.9068 |
| avg_hold_time_bars | 27.3686 |
| exposure | 0.6787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

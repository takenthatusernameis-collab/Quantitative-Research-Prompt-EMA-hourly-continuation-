# EMA Hourly Continuation — VET/USDT P100_144

**Symbol:** VET/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.5118 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 1.0645 |
| gross_win_rate | 0.5136 |
| sharpe_ratio | -4.5326 |
| sortino_ratio | -1.4016 |
| max_drawdown | 0.8265 |
| cagr | -0.4986 |
| net_avg_win | 37.3686 |
| net_avg_loss | -68.0085 |
| avg_hold_time_bars | 4.2296 |
| exposure | 0.0921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

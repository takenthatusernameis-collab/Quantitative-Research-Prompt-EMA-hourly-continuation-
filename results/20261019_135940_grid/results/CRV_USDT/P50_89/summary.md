# EMA Hourly Continuation — CRV/USDT P50_89

**Symbol:** CRV/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.4677 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.8610 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -6.0323 |
| sortino_ratio | -2.2750 |
| max_drawdown | 0.9419 |
| cagr | -0.6733 |
| net_avg_win | 25.3328 |
| net_avg_loss | -45.1567 |
| avg_hold_time_bars | 4.2134 |
| exposure | 0.1373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — INJ/USDT P50_144

**Symbol:** INJ/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.5992 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.8435 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -3.5007 |
| sortino_ratio | -1.0828 |
| max_drawdown | 0.7331 |
| cagr | -0.4041 |
| net_avg_win | 48.7622 |
| net_avg_loss | -69.0048 |
| avg_hold_time_bars | 10.5391 |
| exposure | 0.2328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — KNC/USDT P50_144

**Symbol:** KNC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.5895 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 0.9404 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -3.5491 |
| sortino_ratio | -1.0824 |
| max_drawdown | 0.7476 |
| cagr | -0.4060 |
| net_avg_win | 46.5735 |
| net_avg_loss | -71.3885 |
| avg_hold_time_bars | 13.8101 |
| exposure | 0.2975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

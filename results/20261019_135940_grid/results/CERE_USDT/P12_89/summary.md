# EMA Hourly Continuation — CERE/USDT P12_89

**Symbol:** CERE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 834 |
| net_profit_factor | 0.4643 |
| net_win_rate | 0.3825 |
| gross_profit_factor | 0.7633 |
| gross_win_rate | 0.4089 |
| sharpe_ratio | -9.0635 |
| sortino_ratio | -3.6807 |
| max_drawdown | 0.9920 |
| cagr | -0.8493 |
| net_avg_win | 26.9330 |
| net_avg_loss | -35.9326 |
| avg_hold_time_bars | 13.3693 |
| exposure | 0.5068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

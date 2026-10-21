# EMA Hourly Continuation — QI/USDT P20_55

**Symbol:** QI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.7364 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0266 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -2.3682 |
| sortino_ratio | -0.8289 |
| max_drawdown | 0.6491 |
| cagr | -0.3151 |
| net_avg_win | 56.9038 |
| net_avg_loss | -79.3722 |
| avg_hold_time_bars | 8.1795 |
| exposure | 0.2206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

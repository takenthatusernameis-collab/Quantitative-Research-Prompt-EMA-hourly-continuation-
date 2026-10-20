# EMA Hourly Continuation — MEW/USDT P20_21

**Symbol:** MEW/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1185 |
| net_profit_factor | 0.2355 |
| net_win_rate | 0.3165 |
| gross_profit_factor | 0.6354 |
| gross_win_rate | 0.3882 |
| sharpe_ratio | -16.2135 |
| sortino_ratio | -8.2615 |
| max_drawdown | 1.0000 |
| cagr | -0.9901 |
| net_avg_win | 8.2128 |
| net_avg_loss | -16.1478 |
| avg_hold_time_bars | 1.7013 |
| exposure | 0.0916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

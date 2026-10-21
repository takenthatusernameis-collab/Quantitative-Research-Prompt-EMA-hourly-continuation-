# EMA Hourly Continuation — ERG/USDT P89_100

**Symbol:** ERG/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 79 |
| net_profit_factor | 0.3677 |
| net_win_rate | 0.3418 |
| gross_profit_factor | 0.5171 |
| gross_win_rate | 0.3418 |
| sharpe_ratio | -2.6385 |
| sortino_ratio | -0.3334 |
| max_drawdown | 0.3225 |
| cagr | -0.1436 |
| net_avg_win | 69.4649 |
| net_avg_loss | -98.0803 |
| avg_hold_time_bars | 8.1646 |
| exposure | 0.0293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

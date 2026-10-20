# EMA Hourly Continuation — ETN/USDT P20_89

**Symbol:** ETN/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.3821 |
| net_win_rate | 0.3641 |
| gross_profit_factor | 0.5810 |
| gross_win_rate | 0.3779 |
| sharpe_ratio | -8.8789 |
| sortino_ratio | -3.6806 |
| max_drawdown | 0.9770 |
| cagr | -0.8328 |
| net_avg_win | 22.8747 |
| net_avg_loss | -34.2860 |
| avg_hold_time_bars | 8.8648 |
| exposure | 0.3491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

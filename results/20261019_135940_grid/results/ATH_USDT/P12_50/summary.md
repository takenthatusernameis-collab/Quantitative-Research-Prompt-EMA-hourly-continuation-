# EMA Hourly Continuation — ATH/USDT P12_50

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1018 |
| net_profit_factor | 0.6362 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 1.0012 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -4.9722 |
| sortino_ratio | -2.3057 |
| max_drawdown | 0.9295 |
| cagr | -0.6700 |
| net_avg_win | 32.4647 |
| net_avg_loss | -49.0661 |
| avg_hold_time_bars | 6.5088 |
| exposure | 0.3212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

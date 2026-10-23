# EMA Hourly Continuation — CHR/USDT P55_144

**Symbol:** CHR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.6647 |
| net_win_rate | 0.4827 |
| gross_profit_factor | 0.9526 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -2.9151 |
| sortino_ratio | -0.9410 |
| max_drawdown | 0.6966 |
| cagr | -0.3557 |
| net_avg_win | 52.9191 |
| net_avg_loss | -74.2894 |
| avg_hold_time_bars | 11.7673 |
| exposure | 0.2769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

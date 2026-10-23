# EMA Hourly Continuation — GMX/USDT P55_144

**Symbol:** GMX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.5838 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.8812 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -4.2599 |
| sortino_ratio | -1.3959 |
| max_drawdown | 0.8133 |
| cagr | -0.4827 |
| net_avg_win | 47.6764 |
| net_avg_loss | -64.7888 |
| avg_hold_time_bars | 10.3067 |
| exposure | 0.2520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

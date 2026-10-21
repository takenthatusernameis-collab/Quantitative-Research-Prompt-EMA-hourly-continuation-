# EMA Hourly Continuation — NMR/USDT P26_144

**Symbol:** NMR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.7682 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 0.9650 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -1.7663 |
| sortino_ratio | -0.5177 |
| max_drawdown | 0.5059 |
| cagr | -0.2126 |
| net_avg_win | 71.8900 |
| net_avg_loss | -90.9620 |
| avg_hold_time_bars | 25.1635 |
| exposure | 0.4827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

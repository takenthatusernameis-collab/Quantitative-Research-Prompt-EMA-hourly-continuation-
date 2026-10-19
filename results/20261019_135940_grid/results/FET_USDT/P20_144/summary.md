# EMA Hourly Continuation — FET/USDT P20_144

**Symbol:** FET/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7439 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 0.9971 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -1.7818 |
| sortino_ratio | -0.5244 |
| max_drawdown | 0.4924 |
| cagr | -0.2214 |
| net_avg_win | 61.6210 |
| net_avg_loss | -83.9759 |
| avg_hold_time_bars | 29.0709 |
| exposure | 0.5775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

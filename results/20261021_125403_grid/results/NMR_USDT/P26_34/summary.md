# EMA Hourly Continuation — NMR/USDT P26_34

**Symbol:** NMR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.6653 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 1.0266 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -2.3171 |
| sortino_ratio | -0.5730 |
| max_drawdown | 0.5033 |
| cagr | -0.2298 |
| net_avg_win | 65.0556 |
| net_avg_loss | -96.4648 |
| avg_hold_time_bars | 5.3851 |
| exposure | 0.0725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

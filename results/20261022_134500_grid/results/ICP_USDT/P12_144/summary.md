# EMA Hourly Continuation — ICP/USDT P12_144

**Symbol:** ICP/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.6731 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9708 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -2.6660 |
| sortino_ratio | -0.7922 |
| max_drawdown | 0.6273 |
| cagr | -0.3126 |
| net_avg_win | 57.8664 |
| net_avg_loss | -82.1858 |
| avg_hold_time_bars | 35.3986 |
| exposure | 0.7144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

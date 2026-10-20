# EMA Hourly Continuation — NMR/USDT P100_144

**Symbol:** NMR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.4267 |
| net_win_rate | 0.4277 |
| gross_profit_factor | 0.8598 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -6.2857 |
| sortino_ratio | -2.0121 |
| max_drawdown | 0.9217 |
| cagr | -0.6356 |
| net_avg_win | 31.2891 |
| net_avg_loss | -54.8122 |
| avg_hold_time_bars | 4.9922 |
| exposure | 0.1162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

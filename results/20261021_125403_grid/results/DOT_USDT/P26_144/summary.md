# EMA Hourly Continuation — DOT/USDT P26_144

**Symbol:** DOT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.8374 |
| net_win_rate | 0.5100 |
| gross_profit_factor | 1.0426 |
| gross_win_rate | 0.5100 |
| sharpe_ratio | -1.0587 |
| sortino_ratio | -0.2847 |
| max_drawdown | 0.3559 |
| cagr | -0.1243 |
| net_avg_win | 81.5729 |
| net_avg_loss | -101.3751 |
| avg_hold_time_bars | 30.1709 |
| exposure | 0.4814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

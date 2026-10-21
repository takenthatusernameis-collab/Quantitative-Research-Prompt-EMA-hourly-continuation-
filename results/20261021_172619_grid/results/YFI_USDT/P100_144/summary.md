# EMA Hourly Continuation — YFI/USDT P100_144

**Symbol:** YFI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.5037 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.8283 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -3.7241 |
| sortino_ratio | -0.9514 |
| max_drawdown | 0.6776 |
| cagr | -0.3530 |
| net_avg_win | 47.3197 |
| net_avg_loss | -77.2010 |
| avg_hold_time_bars | 6.4132 |
| exposure | 0.0920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

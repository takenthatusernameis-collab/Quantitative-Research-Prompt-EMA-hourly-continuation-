# EMA Hourly Continuation — WIF/USDT P12_89

**Symbol:** WIF/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.6664 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.9316 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -4.2176 |
| sortino_ratio | -1.6009 |
| max_drawdown | 0.8617 |
| cagr | -0.5382 |
| net_avg_win | 50.3032 |
| net_avg_loss | -65.4755 |
| avg_hold_time_bars | 15.7432 |
| exposure | 0.5238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ACE/USDT P26_100

**Symbol:** ACE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.8178 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0368 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -1.2689 |
| sortino_ratio | -0.3783 |
| max_drawdown | 0.3695 |
| cagr | -0.1608 |
| net_avg_win | 72.2682 |
| net_avg_loss | -92.5333 |
| avg_hold_time_bars | 16.9931 |
| exposure | 0.3337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

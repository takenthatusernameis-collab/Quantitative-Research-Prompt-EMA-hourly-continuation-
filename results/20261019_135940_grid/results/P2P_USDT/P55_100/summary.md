# EMA Hourly Continuation — P2P/USDT P55_100

**Symbol:** P2P/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.4491 |
| net_win_rate | 0.3965 |
| gross_profit_factor | 0.6733 |
| gross_win_rate | 0.4000 |
| sharpe_ratio | -5.6409 |
| sortino_ratio | -1.8891 |
| max_drawdown | 0.9045 |
| cagr | -0.6038 |
| net_avg_win | 32.2579 |
| net_avg_loss | -47.1961 |
| avg_hold_time_bars | 5.8226 |
| exposure | 0.1522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

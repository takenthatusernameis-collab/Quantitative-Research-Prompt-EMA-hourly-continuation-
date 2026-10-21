# EMA Hourly Continuation — BONK/USDT P26_50

**Symbol:** BONK/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.8863 |
| net_win_rate | 0.5328 |
| gross_profit_factor | 1.1326 |
| gross_win_rate | 0.5328 |
| sharpe_ratio | -0.7013 |
| sortino_ratio | -0.1898 |
| max_drawdown | 0.2915 |
| cagr | -0.0864 |
| net_avg_win | 84.6507 |
| net_avg_loss | -108.9012 |
| avg_hold_time_bars | 6.7806 |
| exposure | 0.1082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

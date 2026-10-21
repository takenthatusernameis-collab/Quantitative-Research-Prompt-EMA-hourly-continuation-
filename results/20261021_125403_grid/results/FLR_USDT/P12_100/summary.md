# EMA Hourly Continuation — FLR/USDT P12_100

**Symbol:** FLR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.7745 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0012 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -1.8401 |
| sortino_ratio | -0.6411 |
| max_drawdown | 0.5466 |
| cagr | -0.2561 |
| net_avg_win | 60.4262 |
| net_avg_loss | -79.3505 |
| avg_hold_time_bars | 18.0677 |
| exposure | 0.4854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

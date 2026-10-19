# EMA Hourly Continuation — SEI/USDT P20_100

**Symbol:** SEI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.7308 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 1.0641 |
| gross_win_rate | 0.5058 |
| sharpe_ratio | -2.8371 |
| sortino_ratio | -0.9794 |
| max_drawdown | 0.7301 |
| cagr | -0.3724 |
| net_avg_win | 63.2333 |
| net_avg_loss | -84.5322 |
| avg_hold_time_bars | 17.0367 |
| exposure | 0.4639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

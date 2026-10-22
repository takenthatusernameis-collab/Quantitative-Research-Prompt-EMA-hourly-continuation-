# EMA Hourly Continuation — BTC/USDT P20_26

**Symbol:** BTC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1300 |
| net_profit_factor | 0.0779 |
| net_win_rate | 0.2408 |
| gross_profit_factor | 0.8499 |
| gross_win_rate | 0.4108 |
| sharpe_ratio | -19.9848 |
| sortino_ratio | -11.1788 |
| max_drawdown | 1.0000 |
| cagr | -0.9979 |
| net_avg_win | 2.6976 |
| net_avg_loss | -10.9872 |
| avg_hold_time_bars | 2.0423 |
| exposure | 0.1062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

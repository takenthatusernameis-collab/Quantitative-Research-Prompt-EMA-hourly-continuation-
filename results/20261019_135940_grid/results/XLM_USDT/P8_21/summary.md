# EMA Hourly Continuation — XLM/USDT P8_21

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1770 |
| net_profit_factor | 0.1707 |
| net_win_rate | 0.4130 |
| gross_profit_factor | 0.7323 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -14.7555 |
| sortino_ratio | -8.8117 |
| max_drawdown | 1.0000 |
| cagr | -0.9902 |
| net_avg_win | 2.8154 |
| net_avg_loss | -11.6054 |
| avg_hold_time_bars | 2.7661 |
| exposure | 0.2225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

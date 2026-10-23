# EMA Hourly Continuation — NOT/USDT P26_89

**Symbol:** NOT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 722 |
| net_profit_factor | 0.6047 |
| net_win_rate | 0.4584 |
| gross_profit_factor | 0.9091 |
| gross_win_rate | 0.4584 |
| sharpe_ratio | -5.1620 |
| sortino_ratio | -1.9772 |
| max_drawdown | 0.9053 |
| cagr | -0.6171 |
| net_avg_win | 41.7262 |
| net_avg_loss | -58.4174 |
| avg_hold_time_bars | 8.6399 |
| exposure | 0.2930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

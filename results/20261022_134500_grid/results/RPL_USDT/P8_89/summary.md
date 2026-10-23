# EMA Hourly Continuation — RPL/USDT P8_89

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.7447 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 1.0060 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -2.6720 |
| sortino_ratio | -0.9652 |
| max_drawdown | 0.6900 |
| cagr | -0.3678 |
| net_avg_win | 61.9160 |
| net_avg_loss | -79.9207 |
| avg_hold_time_bars | 21.4294 |
| exposure | 0.6391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

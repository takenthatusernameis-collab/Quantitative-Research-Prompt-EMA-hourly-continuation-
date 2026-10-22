# EMA Hourly Continuation — TAO/USDT P8_12

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1820 |
| net_profit_factor | 0.2923 |
| net_win_rate | 0.3780 |
| gross_profit_factor | 0.6859 |
| gross_win_rate | 0.4027 |
| sharpe_ratio | -16.9653 |
| sortino_ratio | -10.3489 |
| max_drawdown | 1.0000 |
| cagr | -0.9963 |
| net_avg_win | 6.0038 |
| net_avg_loss | -12.4829 |
| avg_hold_time_bars | 1.6780 |
| exposure | 0.1388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — DOT/USDT P12_89

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.6072 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9618 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -3.7607 |
| sortino_ratio | -1.2864 |
| max_drawdown | 0.8037 |
| cagr | -0.4666 |
| net_avg_win | 42.7441 |
| net_avg_loss | -65.1740 |
| avg_hold_time_bars | 22.3065 |
| exposure | 0.6053 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

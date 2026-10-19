# EMA Hourly Continuation — DOT/USDT P21_89

**Symbol:** DOT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.6546 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 1.0678 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -3.5769 |
| sortino_ratio | -1.3001 |
| max_drawdown | 0.8020 |
| cagr | -0.4608 |
| net_avg_win | 45.5244 |
| net_avg_loss | -68.9169 |
| avg_hold_time_bars | 13.1259 |
| exposure | 0.3932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

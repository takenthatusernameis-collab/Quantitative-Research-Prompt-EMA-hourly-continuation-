# EMA Hourly Continuation — SUN/USDT P20_50

**Symbol:** SUN/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 843 |
| net_profit_factor | 0.2934 |
| net_win_rate | 0.3582 |
| gross_profit_factor | 0.8327 |
| gross_win_rate | 0.4247 |
| sharpe_ratio | -11.5898 |
| sortino_ratio | -4.8734 |
| max_drawdown | 0.9984 |
| cagr | -0.9220 |
| net_avg_win | 13.7284 |
| net_avg_loss | -26.1182 |
| avg_hold_time_bars | 7.0320 |
| exposure | 0.2683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

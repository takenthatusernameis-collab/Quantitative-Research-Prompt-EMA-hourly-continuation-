# EMA Hourly Continuation — ACE/USDT P8_89

**Symbol:** ACE/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7728 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9575 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -1.7369 |
| sortino_ratio | -0.5198 |
| max_drawdown | 0.4669 |
| cagr | -0.2131 |
| net_avg_win | 71.0940 |
| net_avg_loss | -88.3370 |
| avg_hold_time_bars | 31.8126 |
| exposure | 0.6378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

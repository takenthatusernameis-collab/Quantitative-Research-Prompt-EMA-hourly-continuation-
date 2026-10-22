# EMA Hourly Continuation — ENS/USDT P21_89

**Symbol:** ENS/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.6468 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9907 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -3.8840 |
| sortino_ratio | -1.4527 |
| max_drawdown | 0.8466 |
| cagr | -0.5014 |
| net_avg_win | 44.0911 |
| net_avg_loss | -64.4111 |
| avg_hold_time_bars | 12.4745 |
| exposure | 0.4003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — WOO/USDT P21_89

**Symbol:** WOO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.8179 |
| net_win_rate | 0.4971 |
| gross_profit_factor | 1.0150 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -1.7136 |
| sortino_ratio | -0.5596 |
| max_drawdown | 0.5734 |
| cagr | -0.2283 |
| net_avg_win | 82.9921 |
| net_avg_loss | -100.3019 |
| avg_hold_time_bars | 15.1536 |
| exposure | 0.3589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

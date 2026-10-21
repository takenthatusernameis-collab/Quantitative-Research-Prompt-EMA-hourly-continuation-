# EMA Hourly Continuation — LUNC/USDT P20_89

**Symbol:** LUNC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.5904 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.7730 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -3.4627 |
| sortino_ratio | -1.1076 |
| max_drawdown | 0.7295 |
| cagr | -0.3994 |
| net_avg_win | 46.0409 |
| net_avg_loss | -62.7243 |
| avg_hold_time_bars | 14.2742 |
| exposure | 0.3290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

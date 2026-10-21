# EMA Hourly Continuation — CARV/USDT P50_89

**Symbol:** CARV/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.6017 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.8479 |
| gross_win_rate | 0.4574 |
| sharpe_ratio | -2.8662 |
| sortino_ratio | -0.7307 |
| max_drawdown | 0.5147 |
| cagr | -0.2849 |
| net_avg_win | 63.1854 |
| net_avg_loss | -88.5035 |
| avg_hold_time_bars | 8.3488 |
| exposure | 0.1212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

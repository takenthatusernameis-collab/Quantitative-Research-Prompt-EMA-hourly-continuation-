# EMA Hourly Continuation — LISTA/USDT P26_34

**Symbol:** LISTA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 925 |
| net_profit_factor | 0.4073 |
| net_win_rate | 0.4173 |
| gross_profit_factor | 0.8668 |
| gross_win_rate | 0.4443 |
| sharpe_ratio | -9.4980 |
| sortino_ratio | -4.2340 |
| max_drawdown | 0.9934 |
| cagr | -0.8826 |
| net_avg_win | 17.6807 |
| net_avg_loss | -31.0898 |
| avg_hold_time_bars | 3.0422 |
| exposure | 0.1376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

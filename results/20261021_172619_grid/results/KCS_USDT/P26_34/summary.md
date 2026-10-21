# EMA Hourly Continuation — KCS/USDT P26_34

**Symbol:** KCS/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 202 |
| net_profit_factor | 0.2235 |
| net_win_rate | 0.3168 |
| gross_profit_factor | 0.5227 |
| gross_win_rate | 0.3317 |
| sharpe_ratio | -5.9644 |
| sortino_ratio | -1.2597 |
| max_drawdown | 0.7786 |
| cagr | -0.4515 |
| net_avg_win | 35.0228 |
| net_avg_loss | -72.6663 |
| avg_hold_time_bars | 5.6535 |
| exposure | 0.0519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

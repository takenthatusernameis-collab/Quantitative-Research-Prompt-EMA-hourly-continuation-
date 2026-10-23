# EMA Hourly Continuation — POKT/USDT P12_20

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1455 |
| net_profit_factor | 0.3236 |
| net_win_rate | 0.3251 |
| gross_profit_factor | 0.8369 |
| gross_win_rate | 0.3553 |
| sharpe_ratio | -15.4646 |
| sortino_ratio | -8.3828 |
| max_drawdown | 1.0000 |
| cagr | -0.9864 |
| net_avg_win | 10.1128 |
| net_avg_loss | -15.0541 |
| avg_hold_time_bars | 2.9759 |
| exposure | 0.1959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

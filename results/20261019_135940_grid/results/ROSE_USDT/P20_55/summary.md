# EMA Hourly Continuation — ROSE/USDT P20_55

**Symbol:** ROSE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 990 |
| net_profit_factor | 0.6264 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 1.0214 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -5.9757 |
| sortino_ratio | -2.6534 |
| max_drawdown | 0.9618 |
| cagr | -0.7189 |
| net_avg_win | 34.9459 |
| net_avg_loss | -48.4192 |
| avg_hold_time_bars | 5.8495 |
| exposure | 0.2632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
